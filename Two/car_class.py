#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-08 15:42:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
'''
类的学习2
'''

class MyCar:
    """第二节教学例子
    一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 60

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        """打印里程"""
        print("This car has %s milies on it." % str(self.odometer_reading))

    def update_odometer(self, mileage):
        """设置里程表的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!")

    def increment_odometer(self, miles):
        """里程表增加"""
        self.odometer_reading += miles


class ElectricCar(MyCar):
    """用汽车类子类化电动汽车"""

    def __init__(self, make, model, year):
        """初始化电动汽车属性
            调用父类初始化"""
        super().__init__( make, model, year)
        self.battery = Battery()


class Battery:
    """模拟电动汽车电瓶"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印电瓶容量的描述信息"""
        print("This car has a %s-kWh battery." % str(self.battery_size))


if __name__ == '__main__':
    car = MyCar('audi', 'a4', 2016)
    msg = car.get_descriptive_name()
    print(msg)
    car.update_odometer(56000)
    car.read_odometer()
    car.increment_odometer(100)
    car.read_odometer()

    My_ECar = ElectricCar('tesla', 'model-s', 2016)
    print(My_ECar.get_descriptive_name())
    My_ECar.battery.describe_battery()
