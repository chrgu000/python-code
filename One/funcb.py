# -*- coding: utf-8 -*-
'''
闭包
'''


def hello_conf(prefix):
    def hello(name):
        print(prefix, name)
    return hello

a = hello_conf('Good Morning')
print(a.__name__)
a('milo')
a('Bob')

b = hello_conf('Good Afternoon ')
print(b.__name__)
b('小明')
