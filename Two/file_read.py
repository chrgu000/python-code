#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-09 17:14:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
文件和异常第一节
10.1 文件
"""

filename = 'pi_digits.txt'

# 打开文件
with open(filename) as file_object:
    """with确保文件妥善的打开和关闭"""

    # 读取所有内容到变量contents
    contents = file_object.read()
    print("读取后返回的类型是：%s\n" % type(contents))
    print("所有内容：\n%s" % contents.rstrip())

# 打开文件
with open(filename) as file_object:
    # 逐行读取
    for line in file_object:
        print(line.rstrip())  # 消除行末位的空白

