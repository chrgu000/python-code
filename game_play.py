# -*- coding: utf-8 -*-

from game_class import *

msg = "欢迎来到英雄无敌的世界！"
print(msg)

g = SignUp()
Loading('注册中')
print('''
        账号：%s
        密码：%s
        请妥善保存！
    ''' % (g.name, g.pwd))

player = Hero()

print(player.name, player.hp, player.act)