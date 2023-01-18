# -*- coding: utf-8 -*-
"""
-------------------------------------------------
变量的作用域：builtin -> module -> local

-------------------------------------------------
"""


count = 10

print(count)


def greeting(flag: bool):
    global count
    if flag:
        count = 20

    print(count)


greeting(True)

print(count)
