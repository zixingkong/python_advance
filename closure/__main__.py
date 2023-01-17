# -*- coding: utf-8 -*-
"""
-------------------------------------------------
闭包

-------------------------------------------------
"""


def greeting():
    message = "hello"
    value = 20

    def inner():
        print(f"{value} - {message}")

    message = "second"

    return inner


f = greeting()
print(f.__closure__)
f()
