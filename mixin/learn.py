# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：   learn
   Description:  
   Date：        2023/1/17
-------------------------------------------------
"""
import json


class MapMixin:
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


class DictMixin:
    def to_dict(self):
        return self.__convert_to_dict(self.__dict__)

    def __convert_to_dict(self, attrs: dict):
        result = {}
        for key, value in attrs.items():
            result[key] = self.__convert_to_value(value)
        return result

    def __convert_to_value(self, value):
        if isinstance(value, DictMixin):
            return self.to_dict()
        elif isinstance(value, dict):
            return self.__convert_to_dict(value)
        elif isinstance(value, list):
            return [self.__convert_to_value(li) for li in value]
        elif hasattr(value, "__dict__"):
            return self.__convert_to_dict(value.__dict__)
        else:
            return value


class JSONMixin:
    def to_json(self):
        return json.dumps(self.to_dict())


class Student(MapMixin, DictMixin, JSONMixin):
    def __init__(self, name, age, li, di):
        self.name = name
        self.age = age
        self.li = li
        self.di = di


s = Student("Jack", 20, [1, 2, 3], {"a": "1", "b": "2", "c": "3"})

print(s["name"])
print(s.to_dict())
print(s.to_json())
