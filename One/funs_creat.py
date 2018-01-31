#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
函数批量生成
'''
button_list = [
                'button_num0',
                'button_num1',
                'button_num2',
                'button_num3',
                'button_num4',
                'button_num5',
                'button_num6',
                'button_num7',
                'button_num8',
                'button_num9',
                'button_and',
                'button_sub',
                'button_mul',
                'button_div',
                'button_equal',
                'button_point'
                ]
button_evt_list = [fun_name+'EVT' for fun_name in button_list]

#print(button_evt_list)

class FuncGen:
    def __init__(self,name):
        self.name = name
    def __call__(self):
        print("hello, i am  %s" % self.name)  # 同样的函数主体
'''原作者用字典update，现在改为列表 append'''
#dictf = {}
dictf = []
for a in button_evt_list:
    #dictf.update({a: FuncGen(a)})
    dictf.append(FuncGen(a))

dictf[0]()
#for a in button_evt_list:
    #dictf[a]()


'''第二个'''
'''
import sys

lista = ["funca","funcb","funcc"]

FUNC_TEMPLATE = "def {func}(): print(\"I'm Han!!\")"

for fn in lista:
    exec(FUNC_TEMPLATE.format(func=fn))

local_vars = dict(locals().items())

funcs = [local_vars[f] for f in lista]

print(funcs[0])
funca()
'''