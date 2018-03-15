#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 14:03:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
'''
类的学习
'''

class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗坐下"""
        print("%s is now sitting." % self.name.title())

    def roll_over(self):
        """模拟小狗打滚"""
        print("%s rolled over!" % self.name.title())


class Restaurant:
    """9-1练习题：餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 统计就餐过的人数
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐馆的名字和菜系"""
        print("\nMy restaurant name is %s, and cuisine type is %s !"
                % (self.restaurant_name.title(), self.cuisine_type))

    def open_restaurant(self):
        """打印餐馆opening"""
        print("Restaurant is open now !")

    def set_number_served(self, number):
        """统计服务过的人数"""
        self.number_served = number
        return self.number_served

    def increment_number_served(self, number, days=1):
        """每天可能接待的人数"""

        print("""
累计接待就餐人数：%d
预计每天接待人数：%d
预计%d天后累计人数：%d
                """ % (
                        self.number_served,
                        number,
                        days, self.number_served + (number * days),
                        ))

class IceCreamStand(Restaurant):
    """子类化冰淇淋小店"""

    def __init__(self, *flavors):
        """初始化属性
        *flavors 接收到的是tuple"""
        self.flavors = flavors

    def describe_IceCream(self):
        """打印所有口味的冰淇淋"""
        #print(type(self.flavors))
        if isinstance(self.flavors, (set, list, tuple, )):
            for flavor in self.flavors:
                print("%s IceCream." % flavor)



class User:
    """9-3习题"""

    def __init__(self, first_name, last_name, **others):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.others = others
        # 声明登录次数
        self.login_attempts = 0

    def describe_user(self):
        """打印用户信息摘要"""
        self.full_name = (self.first_name + " " + self.last_name).title()
        print("name: %s " % self.full_name)
        if self.others:
            for key, value in self.others.items():
                print("%s: %s" % (key,value))

    def greet_user(self):
        """打招呼"""
        print("Hello, %s !" % self.full_name)

    def increment_login_attempts(self):
        """登录次数每次加1"""
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        """登录次数归零"""
        self.login_attempts = 0
        return self.login_attempts

class Administrator(User):
    """管理员，子类化"""

    def __init__(self):
        """初始化属性"""
        self.privileges = Privileges()


class Privileges:
    """用户权限"""

    def __init__(self):
        """初始化属性"""
        self.privileges = ["can add post", "can delete post", 'can ban user']

    def show_privileges(self):
        """打印显示权限"""
        for privilege in self.privileges:
            print(privilege)


if __name__ == '__main__':
    """
    my_dog = Dog('MIMI', 5)
    print("\nMy Dog's name is %s, and it's %d years old!"
            % (my_dog.name.title(), my_dog.age))
    my_dog.sit()
    my_dog.roll_over()

    your_dog = Dog('miaomiao', 2)
    print("\nMy Dog's name is %s, and it's %d years old"
            % (your_dog.name.title(), your_dog.age))
    your_dog.sit()
    your_dog.roll_over()


    my_restaurant = Restaurant('yellow rover', '川')
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
    number_served = my_restaurant.set_number_served(236)
    print("Seved %d peoples!" % number_served)
    my_restaurant.increment_number_served(50, 9)

    ice_cream = IceCreamStand()
    ice_cream.describe_IceCream()"""

    user_bob = User('BOb', 'tang', address='USA', age=22)
    user_bob.describe_user()
    user_bob.greet_user()
    for x in range(4):
        print(user_bob.increment_login_attempts())

    print(user_bob.reset_login_attempts())

    admin = Administrator()
    admin.privileges.show_privileges()
