# -*- coding: utf-8 -*-
'''
4位数的验证码：
    数字、英文大小写
'''
import random

nums = '1234567890'
abc = 'abcdefghijklmnopqrstuvwxyz'


while 1:
    yanZhengMa = ''
    for x in range(4):
        yanZhengMa = yanZhengMa + random.choice(nums + abc + abc.upper())

    print('验证码：', yanZhengMa)
    userInput = input("请输入验证码：")
    if userInput == yanZhengMa:
        print('\n\nCongratulations 验证通过！！\n')
    elif userInput == 'quit':
        break
    else:
        print('\n\nWarning 验证失败！！\n')
