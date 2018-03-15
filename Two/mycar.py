#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-09 15:44:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
类的导入使用
"""
import car_class
# from car_class import *
# from car_class import MyCar, ElectricCar

# from car_class import MyCar 可以省去 car_class.
car = car_class.MyCar('audi', 'a4', 2016)
msg = car.get_descriptive_name()
print(msg)
car.update_odometer(56000)
car.read_odometer()
car.increment_odometer(100)
car.read_odometer()

# from car_class import ElectricCar 可以省去 car_class.
My_ECar = car_class.ElectricCar('tesla', 'model-s', 2016)
print(My_ECar.get_descriptive_name())
My_ECar.battery.describe_battery()
