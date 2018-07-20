#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-03 13:57:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
json
"""
import pickle
import json

def dump_load():
    obj = dict(name='小明', age=20)
    s = json.dumps(obj, ensure_ascii=False)
    #print(s)

    d = dict(name='Bob', age=20, score=88)
    print(pickle.dumps(d))

    with open('dump.txt', 'wb') as f:
        pickle.dump(d, f)

    with open('dump.txt', 'rb') as f:
        print(pickle.load(f))


class Student:
    """用于测试的类"""
    def __init__(self, name, age, score):
        """初始化属性"""
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    """类json化方法"""
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score,

    }

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))