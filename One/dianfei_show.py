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

class ShowFrame(wx.Frame):
    """用于展示数据的新窗口"""

    def  __init__(self, title_name, labels):
        """用于初始化属性"""
        wx.Frame.__init__(self, None, -1, title_name, size=(280, 280))
        self.labels = labels
        self.SetMinSize((280, 280))
        self.SetMaxSize((280, 280))
        self.SetBackgroundColour('red')

        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(5, 10, -1, -1)
        #panel = wx.Panel(self)


        vbox = wx.BoxSizer(wx.VERTICAL)
        # 取得布局和控件列表
        for label in self.labels:
            sizer, windows = self.display_on_frame(label)
            vbox.Add(sizer, 0, wx.ALL|wx.ALIGN_CENTER, 15)


        self.scroll.SetSizer(vbox)

        self.Show()


    def creat_TextCtrl(self, str_word):
        """创建一个只读的静态文本框"""
        text = wx.TextCtrl(self.scroll, -1, str_word, size=(70, 35),
                            style=wx.TE_READONLY|wx.TE_CENTER)
        return text

    def creat_GridSizer(self, data, rows, cols):
        """data布局显示"""

        # 设置布局
        gridsizer = wx.GridSizer(rows=rows, cols=cols, vgap=0, hgap=0)
        #设置背景颜色
        bg_color = [(187, 255, 255),
                (238, 220, 130),
                (132, 112, 255),
                (255, 193, 193)]

        for x in range(len(data)):
            text = self.creat_TextCtrl(str(data[x]))
            if x >= 5 :
                text.SetBackgroundColour(bg_color[x-5])
            elif x >= 1:
                text.SetBackgroundColour(bg_color[x-1])
            gridsizer.Add(text, 1, flag=wx.EXPAND)
        return gridsizer

    def right_index(self):
        """按照从左到右，从上到下的原则
        按照原控件列表的顺序生成一个一一对应的实际位置的序号列表"""
        indexs = []
        index = 5
        for x in range(4):
            for y in range(2):
                indexs.append(index)
                index += 1
            index += 1
        for x in range(4):
            indexs.append(x)
        for x in range(2, 6):
            indexs.append(x*3-2)
        return indexs

    def list_sort(self, windows):
        """根据实际位置的序号列表将控件列表重新排序"""
        n = 0
        for window in windows.copy():
            index = self.right_index()[n]
            windows[index] = window
            n += 1
        return windows

    def display_on_frame(self, labels):
        """返回布局结果"""

        # 用于存入所有的控件
        windows = []
        # 创建整体布局
        sizer = wx.GridBagSizer(hgap=0, vgap=0)

        # 将数据放到相应pos上
        label_step = (1, 5,)
        for row in range(4):
            for col in range(1, 3):
                text = self.creat_TextCtrl(str(labels[row+label_step[col-1]]),)
                windows.append(text)
                sizer.Add(text, pos=(row+2, col))

        titles = {"日期":(0,0),
                "电箱号":(1,0),
                "余电":(1,1),
                "充值":(1,2),
                "506#":(2,0),
                "507#":(3,0),
                "508#":(4,0),
                "509#":(5,0)}

        # 将标题放到相应的pos
        for key,value in titles.items():
            if key == "日期":
                key += ": " + str(labels[0])
                span=(1,3)
            else:
                key = key
                span=(1,1)
            text = self.creat_TextCtrl(key)
            windows.append(text)
            sizer.Add(text, pos=value, span=span, flag=wx.EXPAND)

        # 最后的列和行可扩展
        #title_sizer.AddGrowableCol(2)
        #title_sizer.AddGrowableRow(5)

        # 控件列表按实际显示顺序排序
        windows = self.list_sort(windows)

        # 设置颜色
        #windows[0].SetBackgroundColour((50, 205, 50))
        font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, '微软雅黑')
        windows[0].SetFont(font)
        for x in range(1, 4):
            windows[x].SetBackgroundColour('white')
            windows[x].SetFont(font)

        # 返回布局和按顺序的控件列表
        return sizer, windows


if __name__ == "__main__":
    app = wx.App()

    data = [
            [20170918, 1102, 895, 378, 842, 0, 700, 3700, 2200],
            [20171211, 878, 1187, 951, 1773, 700, 400, 2600, 1300],
            [20170531, 1353, 1231, 1477, 1250, 800, 1000, 3000, 2000],
            ]
    my_frame = ShowFrame("123123", data)
    app.MainLoop()