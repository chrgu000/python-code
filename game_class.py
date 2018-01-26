# -*- coding: utf-8 -*-
'''
游戏的功能模块
'''
import sys, time

class MsgShow:
    '''输出信息'''
    pass



class SignUp:
    '''用户注册'''
    name = None
    pwd = None

    def __init__(self):
        while 1:
            self.name = input('账号：')
            self.pwd = input('密码：')
            if self.name == '' or  self.pwd == '':
                print('\n用户名、密码不能为空，请重新输入！\n')
            else:
                break


class Loading:
    '''读条'''
    def __init__(self, msg, x = 0.5):
        print(msg + '：', end = '')
        for n in range(20):
            print('>', end = '')
            time.sleep(x)
        print('Done!')
        time.sleep(x)



class Hero:
    '''玩家信息生成'''
    name = 'player001'
    hp=100
    act=10

    def __init__(self):
        self.name = input('请输入昵称：')
        if not self.name:
            self.name = 'player001'
        print('英雄 %s 初始化完毕！' % self.name)

    def hit(self, name):
        name.hp -= self.act

    def blood():
        pass


class Element:

    def __init__(self, name = 'NPC001', hp=1000, act=20):
        self.name = name
        self.hp = hp
        self.act = act
        print('BOSS %s 初始化完毕！' % self.name)


if __name__ == '__main__':
    milo = Hero('milo')
    boss = Element('Boss')
    print(boss.hp)
    milo.hit(boss)
    print(boss.hp)