#/usr/bin/env python3
#-*- coding: utf-8 -*-
#此程序绘制一个星条旗
import turtle

class Flag:
    '''画出一个USA国旗'''
    def __init__(self):
        pass

    def wjx(self, weight, color='red'):  #绘制纯色五角星
        turtle.color(color, color)      #画笔填充一个颜色
        turtle.begin_fill()  #开始填充颜色
        #开始绘制
        for x in range(5):
            turtle.forward(weight)
            turtle.right(144)
        turtle.end_fill()  #填充结束
        #绘制结束

    def fx(self, weight, height, color):
        turtle.color(color, color)
        turtle.begin_fill()
        for x in range(2):
            turtle.forward(weight)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
        turtle.end_fill()

    def pen_move(self, x, y):  #移动画笔
        turtle.penup()  #提起画笔
        turtle.goto(x, y)  #移动画笔
        turtle.pendown()  #落下画笔

    def USA(self):
        self.pen_move(-380, 300)
        ###开始绘制红白长条
        y1 = 300
        for x in range(13):
            self.pen_move(-380, y1)
            if x % 2 != 0:
                self.fx(720, 28, 'white')
            else:
                self.fx(720, 28, 'red')
            y1 = y1 - 28
        ###红白相间长条区结束
        self.pen_move(-380, 300)
        ###开始绘制左上角蓝色区域
        self.fx(240, 196, 'blue')

        self.pen_move(-370, 290)
        ###开始绘制纯白小五角星
        x_w, y_w = -370, 288
        for x1 in range(9):
            self.pen_move(x_w, y_w)
            if x1 % 2  == 0:
                n = 6
                x_w = -370
            else:
                n = 5
                x_w = -350
            for x2 in range(n):
                self.pen_move(x_w, y_w)
                self.wjx(20, 'white')
                x_w = x_w + 40

            y_w = y_w - 21

        turtle.done()


if __name__ == '__main__':
    m = Flag()
    m.USA()