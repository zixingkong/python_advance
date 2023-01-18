# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   learn
   Description:  
   Date：        2023/1/18
-------------------------------------------------
"""
from threading import Condition, Thread


class SafeQueue:
    def __init__(self, size: int):
        self.__item_list = list()
        self.__size = size
        self.__item_lock = Condition()

    def put(self, item):
        with self.__item_lock:
            while len(self.__item_list) == self.__size:
                self.__item_lock.wait()
            self.__item_list.insert(0, item)
            self.__item_lock.notify_all()

    def get(self):
        with self.__item_lock:
            while len(self.__item_list) == 0:
                self.__item_lock.wait()
            res = self.__item_list.pop()
            self.__item_lock.notify_all()
            return res


class MsgProducer(Thread):
    def __init__(self, name: str, count: int, queue: SafeQueue):
        super().__init__()
        self.setName(name)
        self.count = count
        self.queue = queue

    def run(self):
        for n in range(self.count):
            msg = f"{self.getName()} - {n}"
            self.queue.put(msg)


class MsgConsumer(Thread):
    def __init__(self, name: str, queue: SafeQueue):
        super().__init__()
        self.setName(name)
        self.queue = queue
        self.setDaemon(True)

    def run(self):
        while True:
            msg = self.queue.get()
            print(f"{self.getName()} - {msg}\n", end="")


queue = SafeQueue(3)
threads = list()
threads.append(MsgProducer("PA", 10, queue))
threads.append(MsgProducer("PB", 10, queue))
threads.append(MsgProducer("PC", 10, queue))

threads.append(MsgConsumer("CA", queue))
threads.append(MsgConsumer("CB", queue))

for t in threads:
    t.start()
