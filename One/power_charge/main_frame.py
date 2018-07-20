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

from info_frame import InfoFrame
import dianfei_functions as df

class MainFrame(wx.Frame):
    """窗口主体"""
    def __init__(self):
        """初始化属性及设置"""
        wx.Frame.__init__(self, None, -1, "公司电费估算器", size=(500,500))

        # 设置窗口最小值和最大值，注意，值是tuple!值是tuple!值是tuple!
        self.SetMinSize((450,400))
        self.SetMaxSize((500,500))
        self.Center()  # 框架居中(会从屏幕中心出现窗口)

        self.style = 1
        self.widgets = []

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

        # 创建画板
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL) # 总框架布局

        # 电表余额布局
        db_sizer = wx.BoxSizer(wx.HORIZONTAL)  # 电表余额总布局横向

        # 电表充值度数布局
        db_sizer2 = wx.BoxSizer(wx.HORIZONTAL)  # 电表余额总布局

        labels = [
                "余电抄写日期", "506#余电",
                "507#余电", "508#余电",
                "509#余电", "506#充值",
                "507#充值", "508#充值",
                "509#充值", "金额(1.3元/度)",
                "天数：",  # index:10,预期天数文本框
                    ]
        # 首先创建文本框
        for i in range(len(labels)):
            if i != 9:  # 9是静态文本框
                text =  df.creat_TextCtrl(panel, "0", self.style)
            else:
                text = df.creat_StaticText(panel, "0")
            # 将文本框添加到控件列表中
            self.widgets.append(text)

        # 将控件添加到BoxSizer中
        widget_pos = [0, 1, 2, 3, 4, 9, 5, 6, 7, 8,]  # 自定义控件顺序
        for x in range(2):
            for y in range(5):
                if x == 0:
                    sizer = db_sizer
                elif x == 1:
                    sizer = db_sizer2
                index = widget_pos[x*5 + y]  # 按照自定义顺序添加控件到布局中
                # 创建并添加
                box_sizer = df.creat_BoxSizer(panel,
                            labels[index],
                            self.widgets[index])
                sizer.Add(box_sizer, 0, wx.ALL|wx.ALIGN_CENTER,2)  # 居中，外边距2

        # 抄电日期为当天日期，写入文本框
        date_today = time.strftime("%Y%m%d",time.localtime())
        self.widgets[0].SetValue(date_today)
        self.widgets[0].SetMaxLength(8)  # 最大长度
        self.widgets[10].SetValue('75')  # 期许天数

        day_label = df.creat_StaticText(panel, "期许使用天数:")
        # 设置一个字体
        #font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, '微软雅黑')
        day_label.SetFont(df.my_font(11, '微软雅黑'))

        btn_labels = ["计算", "保存数据"]  # index:11 12
        for i in range(2):
            button = df.creat_button(panel, btn_labels[i])
            self.widgets.append(button)
        # 保存按钮，初始不可用
        self.widgets[12].Enable(False)

        # 天数、计算、保存按钮布局
        day_sizer = wx.GridSizer(rows=1, cols=0, vgap=10, hgap=10)
        for x in range(4):
            if x == 0:
                widget = day_label
            else:
                widget = self.widgets[x+9]
            day_sizer.Add(widget, flag=wx.ALIGN_CENTER)

        # 文本显示框，多行，只读
        self.text_show = wx.TextCtrl(panel,-1, size=(400,200),
                    style=wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2)

        # 添加控件布局到总体布局中
        vbox.Add(db_sizer, 0, wx.ALL|wx.ALIGN_CENTER,5)  # 居中，外边距5
        vbox.Add(db_sizer2, 0, wx.ALL|wx.ALIGN_CENTER,5)
        vbox.Add(day_sizer, 0, wx.ALL|wx.ALIGN_CENTER,5)
        vbox.Add(self.text_show, 1, wx.ALL|wx.ALIGN_CENTER|wx.EXPAND,15)

        panel.SetSizer(vbox)


         ####################
        # 下边开始绑定按钮事件
        #####################
        self.widgets[0].Bind(wx.EVT_KILL_FOCUS, self.check_date_type)
        self.Bind(wx.EVT_TEXT, self.OnTextChange)
        self.Bind(wx.EVT_MENU, self.menu_exitEVT, self.exit_menu)
        self.Bind(wx.EVT_MENU, self.on_menu_delete, self.data_all_del_menu)
        self.Bind(wx.EVT_MENU, self.history_menuEVT, self.history_menu)
        self.Bind(wx.EVT_BUTTON, self.btn_countEVT, self.widgets[11])
        self.Bind(wx.EVT_BUTTON, self.btn_SaveEVT, self.widgets[12])

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        #for widget in self.widgets[5:9]:
        #    widget.Bind(wx.EVT_TEXT, self.OnTextChange)

        # 状态栏
        statusBar = self.CreateStatusBar()
        statusBar.SetStatusText(self.GetTitle())
        #self.SetRelatedStatusBar(0)

        # 在文本显示区域列出历史充值日期
        df.all_dates(self.text_show)

        # 检查数据文件
        df.check_data_files(self.text_show, self.widgets[11])

    def check_date_type(self, event):
        """日期框输入完毕后检查合法性"""
        df.check_date(self.widgets)

    def OnTextChange(self, event):
        """数据变化进行格式检查"""
        if df.check_data_type(self.widgets):
            df.money_count(self.widgets, self.text_show)
        #print("OnTextChange")

    def btn_SaveEVT(self, event):
        results = df.getValue(self.widgets, self.text_show)
        df.save_data(self.widgets, results, self.text_show)


    def btn_countEVT(self, event):
        """计算按钮事件"""
        #print("btn_countEVT")
        self.text_show.Clear()  # 清除文本显示区内容
        df.data_count(self.widgets, self.text_show)

    def menu_exitEVT(self, event):
        """Close不写到函数里无法正常退出"""
        self.Close()

    def history_menuEVT(self, event):
        self.text_show.Clear()
        df.history_btn(self.text_show)

        InfoFrame(self, "历史充值", df, df.file_read())

    def OnClose(self, event):
        """关闭时"""
        print("Close FatherFrame")
        event.Skip()

    def on_menu_delete(self, event):
        """菜单删除所有记录"""
        df.clear_all_datas(self)
