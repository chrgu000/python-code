#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29 11:34:05
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
'''
用户信息管理系统
'''

import wx
import time
import sys

class MyFrame(wx.Frame):
    """主界面"""
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "用户信息管理系统",
                            size=(600,400),
                            pos=(100,50))

        panel = wx.Panel(self)

        # 主菜单按钮
        self.btn_query = wx.Button(panel, -1, "用户查询", size=(120,50))
        self.btn_change = wx.Button(panel, -1, "用户增改删", size=(120,50))
        self.btn_save = wx.Button(panel, -1, "保存", size=(120,50))

        # 主菜单布局水平
        self.menu_home_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.menu_home_sizer.Add(self.btn_query, proportion=1)
        self.menu_home_sizer.Add(self.btn_change, proportion=1)
        self.menu_home_sizer.Add(self.btn_save, proportion=0)

        # 查询菜单按钮
        self.btn_user_name = wx.Button(panel, -1, "所有用户", size=(80,30))
        self.btn_user_info = wx.Button(panel, -1, "用户信息", size=(80,30))
        self.btn_back = wx.Button(panel, -1, "返回", size=(80,30))

        # 查询菜单布局管理，水平
        self.menu_query_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.menu_query_sizer.Add(self.btn_user_name, proportion=0)
        self.menu_query_sizer.Add(self.btn_user_info, proportion=0)
        self.menu_query_sizer.Add(self.btn_back, proportion=0)

        # 总布局，竖直
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.Add(self.menu_home_sizer, flag=wx.ALIGN_CENTER)
        self.main_sizer.Add(self.menu_query_sizer, flag=wx.ALIGN_CENTER)

        self.main_sizer.Hide(self.menu_query_sizer)  # 隐藏

        # 布局绑定生效
        panel.SetSizer(self.main_sizer)

        # 按钮事件绑定
        self.Bind(wx.EVT_BUTTON, self.btn_backEVT, self.btn_back)  # 查询菜单之返回按钮
        self.Bind(wx.EVT_BUTTON, self.btn_queryEVT, self.btn_query)  # 主菜单之查询按钮

    # 事件
    def btn_backEVT(self, event):
        """查询菜单返回按钮，效果为隐藏查询菜单"""
        self.main_sizer.Hide(self.menu_query_sizer)  # 隐藏查询菜单
        self.main_sizer.Layout()

    def btn_queryEVT(self, event):
        self.main_sizer.Show(self.menu_query_sizer)
        self.main_sizer.Layout()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
