#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-11 14:29:38
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
说明:存储数据之JSON
"""

import json

users = [["张三丰", '男', 120, "武当山"],["张三", '男', 12, "武当"]]

filename = 'file.json'
"""
# 写入文件
with open(filename, 'w') as f_obj:
    json.dump(users, f_obj, ensure_ascii=False)"""

# 读取文件
with open(filename) as f_obj:
    user_new = json.load(f_obj)

print(type(user_new), len(user_new), '\n', user_new)
