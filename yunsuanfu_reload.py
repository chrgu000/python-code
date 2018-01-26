# -*- coding: utf-8 -*-
'''
运算符重载
'''
class Myclass(object):
    """docstring for Myclass"""
    def __init__(self, arg):
        super(Myclass, self).__init__()
        self.arg = arg


class Mylist:
    """docstring for Mylist"""
    __mylist = []
    def __init__(self, *args):
        self.__mylist = []
        for arg in args:
            self.__mylist.append(arg)
        print(self.__mylist)

    def __add__(self, x):  # __add__ 为 + (加法)的固有方法
        for i in range(len(self.__mylist)):
            self.__mylist[i] += x
        return self.__mylist

    def __sub__(self, x):  # __sub__ 为 - (减法)的固有方法
        for i in range(len(self.__mylist)):
            self.__mylist[i] -= x
        return self.__mylist

    def __mul__(self, x):  # __sub__ 为 * (乘法)的固有方法
        for i in range(len(self.__mylist)):
            self.__mylist[i] *= x
        return self.__mylist

    def __div__(self, x):  # __sub__ 为 / (除法)的固有方法
        for i in range(len(self.__mylist)):
            self.__mylist[i] /= x
        return self.__mylist


    def __mod__(self, x):  # __add__ 为 mod (取模)的固有方法
        for i in range(len(self.__mylist)):
            self.__mylist[i] %= x
        return self.__mylist

    def __pow__(self, x):
        pass

    def show(self):  # 用于输出结果
        print(self.__mylist)


if __name__ == '__main__':
    l = Mylist(10, 20, 30, 40, 50)
    l + 10
    l.show()
    l - 11
    l.show()
    l * 10
    l.show()
    l / 10
    l.show()
