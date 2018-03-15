#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01 15:59:17
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
'''
文件与字典
   文件内容是字典形式
'''
import codecs

def load_dict_from_file(filepath):
    _dict = {}
    try:
        with codecs.open(filepath, 'r', 'utf-8') as dict_file:
            for line in dict_file:
                (key, value) = line.strip().split(':')
                #_dict[key] = value  # 值为字符串
                _dict[key] = eval(value)  # 值为列表形式的字符串转换列表

    except IOError as ioerr:
        print("文件 %s 不存在" % (filepath))

    return _dict

def save_dict_to_file(_dict, filepath):
    try:
        with codecs.open(filepath, 'w', 'utf-8') as dict_file:
            for (key,value) in _dict.items():
                dict_file.write('%s:%s\n' % (key, value))
    except IOError as ioerr:
        print("文件 %s 无法创建" % (filepath))

if __name__ == '__main__' :
    _dict = load_dict_from_file ('dict.txt')
    print(_dict)
    save_dict_to_file(_dict, 'dict_copy.txt')
