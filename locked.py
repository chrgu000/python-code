#-*- coding: utf8 -*-
'''
账号上锁，验证三次失败锁定
'''
import os
welcome = 'welcom to Heros !!!'

i = 0
while 1:
    if os.path.isfile('lock.log'):
        print('locked')
        break
        
    userName = input('login:')
    password = input('password:')

    i += 1
    if userName == 'milo' and password == '123':
        pass
    else:
        if i == 3:
            open('lock.log', 'w').write(userName)
            break
        continue
    print(welcome)