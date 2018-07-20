#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-02 15:43:17
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径

"""


import os



def  find(keyword, path, n=0):
    l = []
    os.chdir(path)
    for x in os.listdir('.'):
        relx = os.path.relpath(x, start=r'c:\users\dawang\python-code')
        if os.path.isdir(x) and x[0] != '.':
            l.append(relx)
        if keyword in x:
            n += 1
            print('  ', n, ':', relx)
            #print(x)
    return l, n

def find_by_keyword(keyword, homepath=r'c:\users\dawang\python-code'):

    os.chdir(homepath)
    print(r'根目录："%s\"' % homepath)
    n = 0 # 查找到文件的计数
    dirnames = [x for x in os.listdir(homepath) if os.path.isdir(x) and x[0] != '.']

    for dirname in dirnames:
        os.chdir(homepath)
        l, n = find(keyword, dirname, n)
        if l:
            for x in l:
                dirnames.append(x)

find_by_keyword('dian')

