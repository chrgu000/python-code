#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-26 14:54:15
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
'''
计算器
'''

import wx, sys


class MyFrame(wx.Frame):
    '''主体框架'''
    soces = 0  # 接收并存储结果

    def buttonNum0EVT(self, event):
        self.text_show.AppendText('0')
    def buttonNum1EVT(self, event):
        self.text_show.AppendText('1')
    def buttonNum2EVT(self, event):
        self.text_show.AppendText('2')
    def buttonNum3EVT(self, event):
        self.text_show.AppendText('3')
    def buttonNum4EVT(self, event):
        self.text_show.AppendText('4')
    def buttonNum5EVT(self, event):
        self.text_show.AppendText('5')
    def buttonNum6EVT(self, event):
        self.text_show.AppendText('6')
    def buttonNum7EVT(self, event):
        self.text_show.AppendText('7')
    def buttonNum8EVT(self, event):
        self.text_show.AppendText('8')
    def buttonNum9EVT(self, event):
        self.text_show.AppendText('9')
    def buttonAndEVT(self, event):
        print(self.text_show.GetValue())
        self.soces = int(self.text_show.GetValue()) + self.soces
        self.text_show.SetValue(str(self.soces))
        #self.text_show.SetValue('+')
    def buttonSubEVT(self, event):
        self.text_show.SetValue('-')
    def buttonMulEVT(self, event):
        self.text_show.SetValue('x')
    def buttonDivEVT(self, event):
        self.text_show.SetValue('÷')
    def buttonEqualEVT(self, event):
        self.text_show.SetValue(str(self.soces))
        #self.text_show.SetValue('=')
    def buttonPointEVT(self, event):
        if (self.text_show.GetValue().count('.')<1):
            self.text_show.AppendText('.')

    def __init__(self):  # 初始化
        wx.Frame.__init__(self, None, -1, "计算器", size=(417,620))  # 调用父类初始化

        panel = wx.Panel(self)  # 创建面板
        font_text_show = wx.Font(60,wx.ROMAN,wx.NORMAL,wx.BOLD)
        self.text_show = wx.TextCtrl(panel,-1,
                                    size=(400,100),
                                    pos=(0,0),
                                    style=wx.ALIGN_RIGHT)
        self.text_show.SetFont(font_text_show)

        self.button_num7 = wx.Button(panel,-1,"7",size=(100,120),pos=(0,100))
        self.button_num8 = wx.Button(panel,-1,"8",size=(100,120),pos=(100,100))
        self.button_num9 = wx.Button(panel,-1,"9",size=(100,120),pos=(200,100))
        self.button_div = wx.Button(panel,-1,"÷",size=(100,120),pos=(300,100))
        self.button_num4 = wx.Button(panel,-1,"4",size=(100,120),pos=(0,220))
        self.button_num5 = wx.Button(panel,-1,"5",size=(100,120),pos=(100,220))
        self.button_num6 = wx.Button(panel,-1,"6",size=(100,120),pos=(200,220))
        self.button_mul = wx.Button(panel,-1,"X",size=(100,120),pos=(300,220))
        self.button_num1 = wx.Button(panel,-1,"1",size=(100,120),pos=(0,340))
        self.button_num2 = wx.Button(panel,-1,"2",size=(100,120),pos=(100,340))
        self.button_num3 = wx.Button(panel,-1,"3",size=(100,120),pos=(200,340))
        self.button_sub = wx.Button(panel,-1,"-",size=(100,120),pos=(300,340))
        self.button_point = wx.Button(panel,-1,".",size=(100,120),pos=(0,460))
        self.button_num0 = wx.Button(panel,-1,"0",size=(100,120),pos=(100,460))
        self.button_equal = wx.Button(panel,-1,"=",size=(100,120),pos=(200,460))
        self.button_and = wx.Button(panel,-1,"+",size=(100,120),pos=(300,460))

        self.Bind(wx.EVT_BUTTON, self.buttonNum0EVT, self.button_num0)
        self.Bind(wx.EVT_BUTTON, self.buttonNum1EVT, self.button_num1)
        self.Bind(wx.EVT_BUTTON, self.buttonNum2EVT, self.button_num2)
        self.Bind(wx.EVT_BUTTON, self.buttonNum3EVT, self.button_num3)
        self.Bind(wx.EVT_BUTTON, self.buttonNum4EVT, self.button_num4)
        self.Bind(wx.EVT_BUTTON, self.buttonNum5EVT, self.button_num5)
        self.Bind(wx.EVT_BUTTON, self.buttonNum6EVT, self.button_num6)
        self.Bind(wx.EVT_BUTTON, self.buttonNum7EVT, self.button_num7)
        self.Bind(wx.EVT_BUTTON, self.buttonNum8EVT, self.button_num8)
        self.Bind(wx.EVT_BUTTON, self.buttonNum9EVT, self.button_num9)
        self.Bind(wx.EVT_BUTTON, self.buttonAndEVT, self.button_and)
        self.Bind(wx.EVT_BUTTON, self.buttonSubEVT, self.button_sub)
        self.Bind(wx.EVT_BUTTON, self.buttonMulEVT, self.button_mul)
        self.Bind(wx.EVT_BUTTON, self.buttonDivEVT, self.button_div)
        self.Bind(wx.EVT_BUTTON, self.buttonEqualEVT, self.button_equal)
        self.Bind(wx.EVT_BUTTON, self.buttonPointEVT, self.button_point)



app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()
