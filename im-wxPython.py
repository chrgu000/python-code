#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-26 14:10:48
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
'''
this file for what can do
'''

import wx
import time

class MyFrame(wx.Frame):  # 继承
    def __init__(self):  # 框架初始化
        wx.Frame.__init__(self, None, -1, "IM", size=(520,450))  # 调用父类初始化
        # 开始自定义框架
        panel = wx.Panel(self)  # 创建面板
        # 静态标签
        label_all = wx.StaticText(panel, -1, "All Conterts", pos=(230,0))

        self.text_all = wx.TextCtrl(panel, -1,
                                    size=(480, 200),
                                    pos=(10, 20),
                                    style=wx.TE_MULTILINE|wx.TE_READONLY
                                    )

        label_in = wx.StaticText(panel, -1, "I Say", pos=(230,230))
        self.text_in = wx.TextCtrl(panel, -1,
                                    size=(480, 80),
                                    pos=(10, 250),
                                    style=wx.TE_MULTILINE
                                    )

        self.btn_sent = wx.Button(panel,-1,"Sent",size=(75,25), pos=(160, 350))
        self.btn_clear = wx.Button(panel,-1,"Clear",size=(75,25), pos=(280, 350))
        self.Bind(wx.EVT_BUTTON, self.btnSendEVT, self.btn_sent)
        self.Bind(wx.EVT_BUTTON, self.btnClearEVT, self.btn_clear)

    def btnSendEVT(self,event):
        user_input = self.text_in.GetValue()
        self.text_in.Clear()
        msg_time = time.ctime()
        inmsg = "You (%s):\n%s\n" % (msg_time, user_input)
        self.text_all.AppendText(inmsg)
        #all = self.text_all.GetValue() + '\n' + user_input
        #self.text_all.SetValue(all)

    def btnClearEVT(self,event):
        self.text_all.Clear()

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()