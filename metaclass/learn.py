# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   learn
   Description:  
   Date：        2023/1/17
-------------------------------------------------
"""


class Human(type):
    def __new__(mcs, *args, **kwargs):
        class_ = super().__new__(mcs, *args)
        if kwargs:
            for k, v in kwargs.items():
                setattr(class_, k, v)
        return class_


# 此处后面定义的字典参数是类变量而不是实例变量
class Student(metaclass=Human, country="China", freedom=True):
    pass


print(Student.country)
print(Student.freedom)
print(Student().country)
print(Student().freedom)
Student.country = "New Zealand"
Student.freedom = False

print(Student().country)
print(Student().freedom)
