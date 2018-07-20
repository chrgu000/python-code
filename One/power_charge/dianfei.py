#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 13:57:25
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
'''
公司电费估算器
'''

import wx


from main_frame import MainFrame




app = wx.App()

frame = MainFrame()
app.SetTopWindow(frame)
frame.Show()


app.MainLoop()

