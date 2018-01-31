'''
多态和继承

'''


class Triangle:   # 多态的演示

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height / 2
        return area


class Square:

    def __init__(self, size):
        self.size = size

    def getArea(self):
        area = self.size ** 2
        return area

a = Triangle(5, 5)
print(a.getArea())

b = Square(5)
print(b.getArea())   # 多态演示结束


class Father:   # 继承的演示
    money = 100000
    __money = 2000000000

    def drive(self):
        print('i can drive a car!')


class Mother:
    money = 300000000


class Son(Father, Mother):
    pass

    def pay(self):
        print(self.money)

    def drive(self):  # 二次定义，重载
        print('I can dive tank !!')
        Father.drive(self)   # 再次调用父类方法


tom = Father()
print(tom.money)
tom.drive()

print('#' * 50)

jerry = Son()
print(jerry.money)
jerry.drive()
jerry.pay()
