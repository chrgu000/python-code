# -*- coding: utf-8 -*-
'''
异常处理
    错误、报错
    ：人性化处理错误，保证代码在可控范围内
    ：捕获异常、处理异常
'''
try:
    s = 'hello'
    print(s[1])
except IndexError:
    print('error')
else:
    print('not error')