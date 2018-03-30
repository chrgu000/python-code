#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-27 15:06:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
显示充值历史
类似EXCEL格式的GridBagSizer布局类
"""

import wx


def creat_GridSizer(data, rows, cols):
    """data布局显示"""

    # 设置布局
    gridsizer = wx.GridSizer(rows=rows, cols=cols, vgap=0, hgap=0)
    #设置背景颜色
    bg_color = [(187, 255, 255),
            (238, 220, 130),
            (132, 112, 255),
            (255, 193, 193)]

    for x in range(len(data)):
        text = wx.TextCtrl(panel, -1, str(data[x]), size=(70, 35),
                    style=wx.TE_READONLY|wx.TE_CENTER)
        if x >= 5 :
            text.SetBackgroundColour(bg_color[x-5])
        elif x >= 1:
            text.SetBackgroundColour(bg_color[x-1])
        gridsizer.Add(text, 1, flag=wx.EXPAND)
    return gridsizer

data = [
        [20170918, 1102, 895, 378, 842, 0, 700, 3700, 2200],
        [20171211, 878, 1187, 951, 1773, 700, 400, 2600, 1300],
        [20170531, 1353, 1231, 1477, 1250, 800, 1000, 3000, 2000],
        ]
app = wx.App()

# 根据数据个数及单位尺寸设定窗口大小
size = ((len(data[-1])+0.4)*70, (len(data)+1.5)*35)
print(size)
frame = wx.Frame(None, -1, '123', size=size)
#vbox = wx.BoxSizer(wx.VERTICAL)  # 整体竖向排列

panel = wx.Panel(frame)

# 设置整体垂直布局
vbox = wx.BoxSizer(wx.VERTICAL)

data_titles = ["日期", "电箱号", "余电", "充值", "506#", "507#", "508#", "509#",]
#bg_color = [(187, 255, 255), (238, 220, 130), (132, 112, 255), (255, 193, 193)]

#data.insert(0, data_titles)  # 插入标题到首位
#title_sizer = creat_GridSizer(data_titles, 0, 3)
#vbox.Add(title_sizer, -1, wx.ALIGN_CENTER)
def creat_TextCtrl(str_word):
    """创建一个只读的静态文本框"""
    text = wx.TextCtrl(panel, -1, str_word, size=(70, 25),
                        style=wx.TE_READONLY|wx.TE_CENTER)
    return text

def creat_GridBagSizer(str_word,pos,span=(1,1)):
    """创建单条数据的定点布局"""
    gridbagsizer = wx.GridBagSizer(hgap=0, vgap=0)
    text = creat_TextCtrl(str_word)
    gridbagsizer.Add(text,pos=pos,span=span)
    # 返回布局状态
    return gridbagsizer

def creat_title_sizer(datas,span=(1, 1)):
    """单条数组的最终布局"""
    title_sizer = wx.GridBagSizer(hgap=0, vgap=0)
    titles = {"日期":(0,0),
            "电箱号":(1,0),
            "余电":(1,1),
            "充值":(1,2),
            "506#":(2,0),
            "507#":(3,0),
            "508#":(4,0),
            "509#":(5,0)}
    for key,value in titles.items():
        if key == "日期":
            key += ": " + str(datas[0])
            span=(1,3)
            print(key, span)
        text = creat_TextCtrl(key)
        title_sizer.Add(text, pos=value, span=span)


    return title_sizer


for x in data.copy():
    #text_sizer = creat_GridSizer(x[1:], 0, 2)
    title_sizer = creat_title_sizer(x)
    #vbox.Add(text_sizer, -1, wx.ALL|wx.ALIGN_CENTER)  # 居中
    vbox.Add(title_sizer, -1, wx.ALL|wx.ALIGN_CENTER)

panel.SetSizer(vbox)
frame.Show()
app.MainLoop()