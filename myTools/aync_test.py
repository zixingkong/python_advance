import pandas as pd
import asyncio
import aiohttp
import json

fail_users = []
account_url = ""
staffinfo_url = ""
headers = {
    "Content-Type": "application/json",
}


async def async_post_request(sem, url, json=None, headers=None):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=json, headers=headers) as response:
                return await response.text()


async def async_djuge_user(user_name, sem):
    result_obj = [user_name, False]
    account_data = {"name": user_name}
    staffinfo_data = {
        "name": [user_name],
    }
    try:
        response_acount = await async_post_request(
            sem, account_url, json=account_data, headers=headers
        )
        response_staffinfo = await async_post_request(
            sem, staffinfo_url, json=staffinfo_data, headers=headers
        )
        response_acount = json.loads(response_acount)
        response_staffinfo = json.loads(response_staffinfo)
    except:
        return result_obj
    else:
        if response_acount["code"] == 0:
            if response_acount["data"]["account"]["name"]:
                result_obj[1] = True
    return result_obj


def main():
    num = 1
    task_list = []
    sem = asyncio.Semaphore(100)
    for user in pd.read_csv("./debug.csv", chunksize=1000, usecols=["userName"]):
        user_names = list(user["userName"].drop_duplicates())
        for user_name in user_names:
            print(num, " -> ", user_name)
            task_list.append(
                asyncio.ensure_future(async_djuge_user(user_name, sem)),
            )
            num += 1
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    fail_users = []
    for task in task_list:
        re_obj = task.result()
        if not re_obj[1]:
            fail_users.append(re_obj[0])

    print("result = ", fail_users)
    # if not len(fail_users):
    #     print(fail_users)
    #     with open("result.txt", "w") as f:
    #         f.write(",\n".join(fail_users))


if __name__ == "__main__":
    import time

    start = time.time()
    main()
    end = time.time()
    print("total : %.1fs" % (end - start))
