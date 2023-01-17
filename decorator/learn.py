# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   learn
   Description:  
   Date：        2023/1/17
-------------------------------------------------
"""

# 1. 不带参数的装饰器
def welcome(fn):
    def wrapper(*args, **kwargs):
        print("welcome ")
        fn(*args, **kwargs)

    return wrapper


@welcome
def my_fun(message: str):
    print(f"hello {message}")


my_fun("jack")


# 2. 带参数的装饰器
def welcome2(name: str):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            print(f"Welcome {name}")
            fn(*args, **kwargs)

        return wrapper

    return decorator


@welcome2("tom")
def my_fun_2(message: str):
    print(f"hello {message}")


my_fun_2("mary")
