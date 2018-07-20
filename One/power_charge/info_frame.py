#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-28 18:15:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
说明
"""
import wx

class InfoFrame(wx.Frame):
    """用于展示数据的新窗口"""

    def  __init__(self, parent, title_name, df, data_lists):
        """用于初始化属性"""
        wx.Frame.__init__(self, parent, title=title_name, size=(700, 400),
                    style=wx.CAPTION|wx.CLOSE_BOX)

        self.style = 2
        self.df = df
        self.parent = parent
        self.data_lists = data_lists
        self.data_lists.reverse()  # 倒序排列
        self.SetBackgroundColour('white')  # 设置背景颜色
        # 创建一个列表框显示信息的列表
        self.listBox_label = df.creat_listBox_label(data_lists)
        self.scroll_focus = []

        # 隐藏父窗口
        parent.Show(False)

        # 创建滚动窗口，主要区域，显示历史充值记录
        self.scroll = wx.ScrolledWindow(self, -1, size=(550, 290))
        # 设置滚动速度及区域大小
        self.scroll.SetScrollbars(5, 10, -1, -1)
        #panel = wx.Panel(self)

        # 整体布局方式
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 顶总区域布局
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # 取得布局和控件列表

        self.scroll_sizer, widgets = self.df.datas_sizer(
                        self.scroll,
                        self.data_lists,
                        self.scroll_focus,)

        self.scroll.SetSizer(self.scroll_sizer)
        # 创建列表区域
        self.listBox = wx.ListBox(self, -1,
                    size=(150, 290),
                    choices=[x for x in self.listBox_label],
                    style=0)
        self.listBox.SetFont(df.my_font(14, ''))
        top_sizer.Add(self.listBox)
        top_sizer.Add(self.scroll)

        # 底部添加按钮空间，功能按钮区
        panel = wx.Panel(self, -1, style=wx.BORDER_DOUBLE, size=(700, 80))
        panel.SetBackgroundColour('white')

        # 创建布局方式
        btn_sizer = wx.GridSizer(rows=1, cols=0, hgap=10, vgap=0)
        # 创建按钮并添加到布局内
        self.buttons = []  # 存放按钮
        btn_labels = ["添加数据", "删除数据", "打印", ]
        for i in range(len(btn_labels)):
            button = self.df.creat_button(panel, btn_labels[i], size=(150, 40))
            button.SetFont(self.df.my_font(24, ''))
            self.buttons.append(button)  # 添加到按钮组
            btn_sizer.Add(button, flag=wx.ALIGN_CENTER)

        panel.SetSizer(btn_sizer)
        vbox.Add(top_sizer)
        vbox.Add(panel)
        self.SetSizer(vbox)



        # 状态栏
        statusBar = self.CreateStatusBar()
        statusBar.SetStatusText("根据上一次充值日期计算间隔天数、平均数，\
                根据期许天数(默认75)计算需充值的度数".replace(" "*8,""))

        self.Show()

        # 将窗口提升到窗口层次结构的顶部
        parent.Bind(wx.EVT_ACTIVATE, self.OnParentActivate)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_BUTTON, self.OnAddBtn, self.buttons[0])
        self.Bind(wx.EVT_BUTTON, self.OnDelBtn, self.buttons[1])
        self.Bind(wx.EVT_BUTTON, self.OnPrintBtn, self.buttons[2])
        self.Bind(wx.EVT_LISTBOX, self.OnLeftDown)


    def OnParentActivate(self, event):
        """窗口置顶"""
        if not self:
            return
        self.Raise()
        event.Skip()
        #print(event.GetActive())

    def OnClose(self, event):
        """关闭时显示父窗口"""
        print("Close chiledFrame")
        self.parent.Show(True)
        event.Skip()

    def OnAddBtn(self, event):
        """按钮添加数据"""
        self.Close()
        #self.parent.Show(True)

    def OnDelBtn(self, event):
        """按钮删除数据"""
        print(self.listBox_label)
        print(self.listBox.GetSelection())
        self.df.del_data_btn(self,
                    self.listBox,
                    self.scroll,
                    self.scroll_sizer,
                    self.scroll_focus,
                    self.data_lists,
                    )


    def OnPrintBtn(self, event):
        """按钮打印"""
        pass

    def OnLeftDown(self, event):
        """鼠标右键"""
        #print("鼠标左键按下")
        select = self.listBox.GetSelection()
        #print("选择了：", select)
        self.scroll_focus[select*2].SetFocus()
        self.scroll_focus[select*2+1].SetFocus()

        event.Skip()
