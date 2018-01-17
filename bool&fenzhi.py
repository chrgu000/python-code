#-*- coding: utf-8 -*-
'''
bool与分支，判断输入类型
'''
a = input('随意输入字符：')
try:
    int(a)
    print('您输入的是类型是   int  ：', '%d' % (int(a)))
except ValueError as e:
    if a:
        if isinstance(a, str):
            print('您输入的是类型是   str   ：', '"%s"' % (a))
        else:
            print('no int and no str')
    else:
        print('没有任何输入')

