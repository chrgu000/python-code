#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 10:11:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
'''
this file for what can do
'''

class User:
    """用户简介"""
    def __init__(self, firstname, last_name, **other):
        self.firstname = firstname
        self.last_name = last_name
        self.other = other

    def describe_user(self):
        if self.other:
            for key, value in self.other.items():
                print(key,'：', value)

    def greet_user(self):
        print("Hello, %s !" % (self.firstname+self.last_name))

xiaoming = User('xiao', 'ming', 住址="北京", 年龄=28)

xiaoming.describe_user()
xiaoming.greet_user()