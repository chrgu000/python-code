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
import sys
import time
import datetime
import codecs

class MyFile:
    """文件的读取和写入"""
    def fRead(self,perssion='r'):
        """读取文件并返回列表"""
        self.f = codecs.open('dianfei.db', perssion, 'utf-8')
        self.f.seek(0,)
        self.l = self.f.readlines()
        for x in range(len(self.l)):
            self.l[x] = eval(self.l[x].rstrip('\n'))
        self.f.close()
        self.l = sorted(self.l, key =lambda l:l[0])  # 二维列表用第个按第0列排序
        return self.l

    def fWrite(self, source):
        self.f = codecs.open('dianfei.db', 'a+', 'utf-8')
        #for x in source:
        #    self.f.write(str(x)+'\n')
        self.f.write(str(source)+'\n')  # 一维数组不需要遍历保存, 直接转换为字符串保存
        self.f.close()

class MyFrame(wx.Frame):
    """主体"""
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "公司电费估算器", size=(500,500))
        self.SetMinSize((450,400))  # 窗口最小值，注意，值是tuple!值是tuple!值是tuple!
        self.SetMaxSize((500,500))
        #self.Center()  # 框架居中(会从屏幕中心出现窗口)

        # 添加菜单
        self.menuBar = wx.MenuBar()  # 首先添加菜单栏

        self.file_menu = wx.Menu()
        self.exit_menu = self.file_menu.Append(-1,"exit", "退出系统")  # 下拉子菜单 exit
        self.data_menu = wx.Menu()
        self.history_menu = self.data_menu.Append(-1, "历史充值")
        self.data_all_del_menu = self.data_menu.Append(-1, "清空历史数据")

        self.menuBar.Append(self.file_menu, "File")
        self.menuBar.Append(self.data_menu, "数据")

        self.SetMenuBar(self.menuBar)  # 将菜单栏添加到框架

        # 创建画板
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL) # 总框架布局

        #self.label_506 = wx.StaticText(panel, -1, "506#电表:", size=(80,30))
        # 电表余额文本框
        self.text_data1 = wx.TextCtrl(panel, -1,  size=(80,25))  # 余电抄写日期
        self.today = time.strftime("%Y%m%d",time.localtime())
        self.text_data1.SetValue(self.today)
        self.text_506 = wx.TextCtrl(panel, -1, "0",  size=(80,25))
        self.text_507 = wx.TextCtrl(panel, -1, "0",  size=(80,25))
        self.text_508 = wx.TextCtrl(panel, -1, "0",  size=(80,25))
        self.text_509 = wx.TextCtrl(panel, -1, "0",  size=(80,25))

        # 电表余额布局
        db_sizer = wx.BoxSizer(wx.HORIZONTAL)  # 电表余额总布局

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
        self.day_text = wx.TextCtrl(panel, -1,  "0")
        self.btn_count = wx.Button(panel, -1, "计算")

        self.day_sizer = wx.GridSizer(rows=1, cols=0, vgap=10, hgap=10)
        self.day_sizer.Add(self.btn_ydSave, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        self.day_sizer.Add(self.day_label, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        self.day_sizer.Add(self.day_text, flag=wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        self.day_sizer.Add(self.btn_count,  flag=wx.ALIGN_CENTER_VERTICAL)

        # 文本显示框，多行，只读
        self.text_show = wx.TextCtrl(panel,-1, size=(400,200), style=wx.TE_MULTILINE|wx.TE_READONLY)

        # 添加所有布局到总体中
        vbox.Add(db_sizer, 0, wx.ALL|wx.ALIGN_CENTER,5)  # 居中，外边距5
        vbox.Add(db_sizer2, 0, wx.ALL|wx.ALIGN_CENTER,5)
        vbox.Add(self.day_sizer, 0, wx.ALL|wx.ALIGN_CENTER,5)
        vbox.Add(self.text_show, 1, wx.ALL|wx.ALIGN_CENTER|wx.EXPAND,15)

        panel.SetSizer(vbox)

         ####################
        # 下边开始绑定按钮事件
        #####################
        self.Bind(wx.EVT_BUTTON, self.btn_countEVT, self.btn_count)
        self.Bind(wx.EVT_MENU, self.menu_exitEVT, self.exit_menu)
        self.Bind(wx.EVT_MENU, self.data_all_del_menuEVT, self.data_all_del_menu)
        self.Bind(wx.EVT_MENU, self.history_menuEVT, self.history_menu)
        self.Bind(wx.EVT_BUTTON, self.btn_ydSaveEVT, self.btn_ydSave)

        # 判断是否是历史数据，没有的话提示先录入至少一条
        try:
            open('dianfei.db', 'r')
        except FileNotFoundError:
            self.text_show.SetValue("Erro:\n    至少需要一条历史数据，填写后点击 信息录入")
            retCode = wx.MessageBox("至少需要一条历史数据，填写后点击 信息录入", "Error")


    def getValue(self):
        """得到余电及充值的数据"""
        self.data_sources = [self.text_data1,
                        self.text_506,
                        self.text_507,
                        self.text_508,
                        self.text_509,
                        self.text_506_2,
                        self.text_507_2,
                        self.text_508_2,
                        self.text_509_2
                        ]
        vl =[]
        for x in self.data_sources:
            try:
                x = int(x.GetValue())
            except TypeERROR:
                self.text_show.SetValue("Erro:\n    日期格式、电数全部都应该是数字!")
            vl.append(x)
        #print(vl)
        return vl

    def msgShow(msg):
        self.text_show.Clear()
        if isintance(msg, str):
            self.text_show.AppendText(msg)
        elif isinstance(msg, list):
            for x in msg:
                self.text_show.AppendText(str(x)+'n')
        else:
            wx.MessageBox("错误，请检查填写内容", "Error")

    def getDays(self):
        self.mf = MyFile()
        self.dianfei_list = self.mf.fRead()
        day1 = str(self.dianfei_list[-1][0])
        day2 = self.text_data1.GetValue()
        try:
            d1 = datetime.date(int(day1[:4]),int(day1[4:6]),int(day1[-2:]))
            d2 = datetime.date(int(day2[:4]),int(day2[4:6]),int(day2[-2:]))
            interval_days = (d2-d1).days
            return interval_days
        except TypeERROR:
            pass

    def menu_exitEVT(self, event):
        """Close不写到函数里无法正常退出"""
        self.Close()

    def history_menuEVT(self, event):
        self.text_show.Clear()
        self.msg = ["日期：", "506#：", "507#：", "508#：", "509#：",
                    "506#充值：", "507#充值：", "508#充值：", "509#充值："]
        self.mf = MyFile()
        self.dianfei_list = self.mf.fRead()
        print(self.dianfei_list)
        for x in self.dianfei_list:
            self.text_show.AppendText("""
                +----------------------+
                |--%s%10s--|
                |------------------------|
                | 表箱 |    余电 |  充值 |
                 %s%4d%8d
                 %s%4d%8d
                 %s%4d%8d
                 %s%4d%8d
                """  % (self.msg[0],x[0],
                        self.msg[1],x[1],x[5],
                        self.msg[2],x[2],x[6],
                        self.msg[3],x[3],x[7],
                        self.msg[4],x[4],x[8]))

    def data_all_del_menuEVT(self, event):
        open('dianfei', 'w')

    def btn_ydSaveEVT(self, event):
        self.data_list = self.getValue()
        self.mf = MyFile()
        self.dianfei_list = self.mf.fRead()
        self.mf.fWrite(self.data_list)
        self.text_show.Clear()  # 清除文本显示区内容
        self.msg = ["日期：", "506#余电：", "507#余电：", "508#余电：", "509#余电：",
                    "506#充值：", "507#充值：", "508#充值：", "509#充值："]
        for x in range(len(self.data_list)):
            if x == (0 or 5 or 9) :
                self.text_show.AppendText("==================\n")
            self.text_show.AppendText(self.msg[x]+str(self.data_list[x])+'\n')

        # 保存提示成功后文本框归零
        self.text_show.AppendText("添加成功！！！")
        #for x in self.data_sources:
        #    x.SetValue('0')  #


    def btn_countEVT(self, event):
        self.text_show.Clear()  # 清除文本显示区内容
        self.mf = MyFile()
        dl = self.mf.fRead()[-1]
        print(dl)
        self.data_list = self.getValue()[0:5]
        #self.data_list =self.data_list
        #print(self.data_list)
        self.msg = ["日期：", "506#余电：", "507#余电：", "508#余电：", "509#余电："]
        for x in range(len(self.data_list)):
            self.text_show.AppendText(self.msg[x]+str(self.data_list[x])+'\n')

        days = self.getDays()  # 获取两个日期的相差天数
        # 计算希望使用多少天需要多少电数
        # 上一次电费的余额加上充值数再减去本次余电数，除以用过的天数，乘以希望用的天数
        # int 取整
        result_506 = int((dl[1]+dl[5]-int(self.text_506.GetValue()))/days)*int(self.day_text.GetValue())
        result_507 = int((dl[2]+dl[6]-int(self.text_507.GetValue()))/days)*int(self.day_text.GetValue())
        result_508 = int((dl[3]+dl[7]-int(self.text_508.GetValue()))/days)*int(self.day_text.GetValue())
        result_509 = int((dl[4]+dl[8]-int(self.text_509.GetValue()))/days)*int(self.day_text.GetValue())
        # 计算充值需要的金额，单价为1.3元/度
        result_cost = (result_506+result_507+result_508+result_509)*1.3
        # 将值写入充值框
        self.text_506_2.SetValue(str(result_506))
        self.text_507_2.SetValue(str(result_507))
        self.text_508_2.SetValue(str(result_508))
        self.text_509_2.SetValue(str(result_509))
        self.text_cost.SetLabel(str(result_cost))


if __name__ == "__main__":
    app = wx.App()

    frame = MyFrame()
    frame.Show()

    app.MainLoop()

