# -*- coding: utf-8 -*-
'''
面向对象
    类（方法、属性）---->>>实例
    公有属性：名字  》》外部可调用的
    私有属性：__名字   （两个下划线开头）》》仅内部
    公有方法： def funName():
    私有方法： def __funName():
    def __init__()  初始化，可传参
'''


class Car:   # 类， 首字母大小
    color = ''

    def run(self):
        print('Go GO GO ! ! !')

'''
bmw = Car()
bmw.color = 'red'
bmw.run()
'''


class Human:
    # Human.__doc__
    '''
        This is the Human class docstring!!
    '''
    name = 'ren'   # 公用属性，外部点化法调用
    gender = 'male'
    age = 25
    __money = 8888  # 私有属性，外部不可直接调用

    def __init__(self, name, age):
        print("<-" * 20)
        self.name = name
        self.age = age
        print('=>' * 20)

    #@classmethod   # 类方法装饰器
    @property
    def say(self):   # 公有方法
        print("I'm %s , %d years old. I have %d a month." % (self.name, self.age, self.__money))
        #self.__lie()
        return self.name

    def __lie(self):
        print('i have 5000')

    @staticmethod  # 加上后不需要对象化，类可直接访问
    def bye():
        print('Game Over !!')


tom = Human('tom', 42)
tom.say