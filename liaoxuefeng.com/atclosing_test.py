#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#Authon: WangBai

"""
如果一个对象没有实现上下文，我们就不能把它用于with语句。
这个时候，可以用closing()来把该对象变为上下文对象。
例如，用with语句使用urlopen():
"""

from contextlib import closing
from urllib.request import urlopen


with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)