#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20 09:52:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
窗口布局
"""
import wx
import time

import dianfei_functions as df


class MyFrame(wx.Frame):
    """窗口主体"""
    def __init__(self):
        """初始化属性及设置"""
        wx.Frame.__init__(self, None, -1, "公司电费估算器", size=(500,500))

        # 设置窗口最小值和最大值，注意，值是tuple!值是tuple!值是tuple!
        self.SetMinSize((450,400))
        self.SetMaxSize((500,500))
        #self.Center()  # 框架居中(会从屏幕中心出现窗口)

    def menu_bar(self):
        """添加菜单栏"""

        # 首先添加菜单栏
        self.menuBar = wx.MenuBar()
        # 添加菜单项
        self.file_menu = wx.Menu()
        # 下拉子菜单 exit
        self.exit_menu = self.file_menu.Append(-1,"exit", "退出系统")
        # 添加菜单项
        self.data_menu = wx.Menu()
        self.history_menu = self.data_menu.Append(-1, "历史充值")
        self.data_all_del_menu = self.data_menu.Append(-1, "清空历史数据")

        # 添加File、数据菜单
        self.menuBar.Append(self.file_menu, "File")
        self.menuBar.Append(self.data_menu, "数据")

        # 将菜单栏添加到框架
        self.SetMenuBar(self.menuBar)

    def form_sizer(self):
        """主体内容布局"""

        # 创建画板
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL) # 总框架布局

        #self.label_506 = wx.StaticText(panel, -1, "506#电表:", size=(80,30))
        # 电表余额文本框
        self.text_data1 = wx.TextCtrl(panel, -1,  size=(80,25))  # 余电抄写日期
        data_today = time.strftime("%Y%m%d",time.localtime())
        self.text_data1.SetValue(data_today)
        self.text_506 = wx.TextCtrl(panel, -1, "0",  size=(80,25))
        self.text_507 = wx.TextCtrl(panel, -1, "0",  size=(80,25))
        self.text_508 = wx.TextCtrl(panel, -1, "0",  size=(80,25))
        self.text_509 = wx.TextCtrl(panel, -1, "0",  size=(80,25))

        # 电表余额布局
        db_sizer = wx.BoxSizer(wx.HORIZONTAL)  # 电表余额总布局横向

        box_data1 = wx.StaticBox(panel, -1, "余电抄写日期")
        box_data1_sizer = wx.StaticBoxSizer(box_data1, wx.VERTICAL)
        box_data1_sizer.Add(self.text_data1)
        box_506 = wx.StaticBox(panel, -1, "506#余电")
        box_506_sizer = wx.StaticBoxSizer(box_506, wx.VERTICAL)
        box_506_sizer.Add(self.text_506)
        box_507 = wx.StaticBox(panel, -1, "507#余电")
        box_507_sizer = wx.StaticBoxSizer(box_507, wx.VERTICAL)
        box_507_sizer.Add(self.text_507)
        box_508 = wx.StaticBox(panel, -1, "508#余电")
        box_508_sizer = wx.StaticBoxSizer(box_508, wx.VERTICAL)
        box_508_sizer.Add(self.text_508)
        box_509 = wx.StaticBox(panel, -1, "509#余电")
        box_509_sizer = wx.StaticBoxSizer(box_509, wx.VERTICAL)
        box_509_sizer.Add(self.text_509)

        db_sizer.Add(box_data1_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)
        db_sizer.Add(box_506_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)  # 居中，外边距2
        db_sizer.Add(box_507_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)
        db_sizer.Add(box_508_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)
        db_sizer.Add(box_509_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)

        # 电表充值文本框
        self.text_506_2 = wx.TextCtrl(panel, -1, "0",  size=(80,25))
        self.text_507_2 = wx.TextCtrl(panel, -1, "0",  size=(80,25))
        self.text_508_2 = wx.TextCtrl(panel, -1, "0",  size=(80,25))
        self.text_509_2 = wx.TextCtrl(panel, -1, "0",  size=(80,25))
        self.text_cost = wx.StaticText(panel, -1, "0", size=(80,25))

        # 电表充值度数布局
        db_sizer2 = wx.BoxSizer(wx.HORIZONTAL)  # 电表余额总布局

        box_506_2 = wx.StaticBox(panel, -1, "506#充值")
        box_506_2_sizer = wx.StaticBoxSizer(box_506_2, wx.VERTICAL)
        box_506_2_sizer.Add(self.text_506_2)
        box_507_2 = wx.StaticBox(panel, -1, "507#充值")
        box_507_2_sizer = wx.StaticBoxSizer(box_507_2, wx.VERTICAL)
        box_507_2_sizer.Add(self.text_507_2)
        box_508_2 = wx.StaticBox(panel, -1, "508#充值")
        box_508_2_sizer = wx.StaticBoxSizer(box_508_2, wx.VERTICAL)
        box_508_2_sizer.Add(self.text_508_2)
        box_509_2 = wx.StaticBox(panel, -1, "509#充值")
        box_509_2_sizer = wx.StaticBoxSizer(box_509_2, wx.VERTICAL)
        box_509_2_sizer.Add(self.text_509_2)
        box_cost = wx.StaticBox(panel, -1, "金额(1.3元/度)")
        box_cost_sizer = wx.StaticBoxSizer(box_cost, wx.VERTICAL)
        box_cost_sizer.Add(self.text_cost)

        db_sizer2.Add(box_506_2_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)  # 居中，外边距2
        db_sizer2.Add(box_507_2_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)
        db_sizer2.Add(box_508_2_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)
        db_sizer2.Add(box_509_2_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)
        db_sizer2.Add(box_cost_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)

        # 期许充值后可使用天数
        self.btn_ydSave = wx.Button(panel, -1, "信息录入")
        self.day_label = wx.StaticText(panel, -1, "期许使用天数:")
        font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.day_label.SetFont(font)
        self.day_text = wx.TextCtrl(panel, -1,  "60")
        self.btn_count = wx.Button(panel, -1, "计算")

        self.day_sizer = wx.GridSizer(rows=1, cols=0, vgap=10, hgap=10)
        self.day_sizer.Add(self.btn_ydSave, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        self.day_sizer.Add(self.day_label, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        self.day_sizer.Add(self.day_text, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        self.day_sizer.Add(self.btn_count,  flag=wx.ALIGN_CENTER_VERTICAL)

        # 文本显示框，多行，只读
        self.text_show = wx.TextCtrl(panel,-1, size=(400,200),
                    style=wx.TE_MULTILINE|wx.TE_READONLY)

        # 添加所有布局到总体中
        vbox.Add(db_sizer, 0, wx.ALL|wx.ALIGN_CENTER,5)  # 居中，外边距5
        vbox.Add(db_sizer2, 0, wx.ALL|wx.ALIGN_CENTER,5)
        vbox.Add(self.day_sizer, 0, wx.ALL|wx.ALIGN_CENTER,5)
        vbox.Add(self.text_show, 1, wx.ALL|wx.ALIGN_CENTER|wx.EXPAND,15)

        panel.SetSizer(vbox)

         ####################
        # 下边开始绑定按钮事件
        #####################
        self.Bind(wx.EVT_BUTTON, df.btn_countEVT, self.btn_count)
        self.Bind(wx.EVT_MENU, df.menu_exitEVT, self.exit_menu)
        self.Bind(wx.EVT_MENU, df.data_all_del_menuEVT, self.data_all_del_menu)
        self.Bind(wx.EVT_MENU, df.history_menuEVT, self.history_menu)
        self.Bind(wx.EVT_BUTTON, df.btn_ydSaveEVT, self.btn_ydSave)

        # 判断是否是历史数据，没有的话提示先录入至少一条
        try:
            open('dianfei.db', 'r')
        except FileNotFoundError:
            self.text_show.SetValue("Erro:\n\t\
                        至少需要一条历史数据，填写后点击 信息录入")
            retCode = wx.MessageBox("至少需要一条历史数据，\
                        填写后点击 信息录入", "Error")
