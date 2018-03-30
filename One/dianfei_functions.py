#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
电费计算的方法
"""
import codecs

from dianfei_ui import MyFrame


def file_read(perssion='r'):
    """读取文件并返回列表"""
    f = codecs.open('dianfei.db', perssion, 'utf-8')
    f.seek(0,)
    l = f.readlines()
    for x in range(len(l)):
        l[x] = eval(l[x].rstrip('\n'))
    f.close()
    l = sorted(l, key =lambda l:l[0])  # 二维列表用第个按第0列排序
    return l

def file_write(source):
    """向文件尾部添加内容"""
    f = codecs.open('dianfei.db', 'a+', 'utf-8')
    #for x in source:
    #    f.write(str(x)+'\n')
    f.write(str(source)+'\n')  # 一维数组不需要遍历保存, 直接转换为字符串保存
    f.close()

def data_all_del_menuEVT(event):
        withopen('dianfei', 'w')

def btn_ydSaveEVT(event):
    data_all_list = getValue()
    dianfei_list = file_read()
    file_write(data_all_list)
    self.text_show.Clear()  # 清除文本显示区内容
    msg_list = ["日期：",
            "506#余电：", "507#余电：",
            "508#余电：", "509#余电：",
            "506#充值：", "507#充值：",
            "508#充值：", "509#充值："]
    for x in range(len(data_all_list)):
        if x == (0 or 5 or 9) :
            self.text_show.AppendText("==================\n")
        self.text_show.AppendText(msg_list[x]+str(data_all_list[x])+'\n')

    # 保存提示成功后文本框归零
    self.text_show.AppendText("添加成功！！！")
    #for x in data_sources:
    #    x.SetValue('0')  #


def btn_countEVT(event):
    self.text_show.Clear()  # 清除文本显示区内容
    dl = file_read()[-1]
    print(dl)
    data_list = getValue()[0:5]
    #print(data_list)
    msg = ["日期：", "506#余电：", "507#余电：", "508#余电：", "509#余电："]
    for x in range(len(data_list)):
        self.text_show.AppendText(msg[x]+str(data_list[x])+'\n')

    days = getDays()  # 获取两个日期的相差天数
    # 计算希望使用多少天需要多少电数
    # 上一次电费的余额加上充值数再减去本次余电数，除以用过的天数，乘以希望用的天数
    # int 取整
    result_506 = round(int((dl[1]+dl[5]-int(self.text_506.GetValue()))/days)
                        * int(self.day_text.GetValue()), -2)
    result_507 = round(int((dl[2]+dl[6]-int(self.text_507.GetValue()))/days)
                        *int(self.day_text.GetValue()), -2)
    result_508 = round(int((dl[3]+dl[7]-int(self.text_508.GetValue()))/days)
                    *int(self.day_text.GetValue()), -2)
    result_509 = round(int((dl[4]+dl[8]-int(self.text_509.GetValue()))/days)
        *int(self.day_text.GetValue()), -2)
    # 计算充值需要的金额，单价为1.3元/度
    result_cost = (result_506+result_507+result_508+result_509)*1.3
    # 将值写入充值框
    self.text_506_2.SetValue(str(result_506))
    self.text_507_2.SetValue(str(result_507))
    self.text_508_2.SetValue(str(result_508))
    self.text_509_2.SetValue(str(result_509))
    self.text_cost.SetLabel(str(result_cost))

def getValue(self):
    """得到余电及充值的数据"""
    data_sources = [self.text_data1,
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
    for x in data_sources:
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

def getDays():
    dianfei_list = file_read()
    day1 = str(dianfei_list[-1][0])
    day2 = self.text_data1.GetValue()
    try:
        d1 = datetime.date(int(day1[:4]),int(day1[4:6]),int(day1[-2:]))
        d2 = datetime.date(int(day2[:4]),int(day2[4:6]),int(day2[-2:]))
        interval_days = (d2-d1).days
        return interval_days
    except TypeERROR:
        pass

def menu_exitEVT(event):
    """Close不写到函数里无法正常退出"""
    self.Close()

def history_menuEVT(event):
    self.text_show.Clear()
    msg = ["日期：", "506#：", "507#：", "508#：", "509#：",
                "506#充值：", "507#充值：", "508#充值：", "509#充值："]
    dianfei_list = file_read()
    print(dianfei_list)
    '''for x in self.dianfei_list:
        self.text_show.AppendText("""
            +----------------------+
            |--%s%10s--|
            |------------------------|
            | 表箱 |    余电 |  充值 |
             %s%4d%8d
             %s%4d%8d
             %s%4d%8d
             %s%4d%8d
            """  % (msg[0],x[0],
                    msg[1],x[1],x[5],
                    msg[2],x[2],x[6],
                    msg[3],x[3],x[7],
                    msg[4],x[4],x[8]))'''
    for x in dianfei_list:
        self.text_show.AppendText("""
            +----------------------+
            |--{}{:^10}--|
            |------------------------|
            | 表箱 |   余电  |  充值 |
             {}{:<6}{:>8}
             {}{:<6}{:>8}
             {}{:<6}{:>8}
             {}{:<6}{:>8}
            """.format(msg[0],x[0],
                    msg[1],x[1],x[5],
                    msg[2],x[2],x[6],
                    msg[3],x[3],x[7],
                    msg[4],x[4],x[8]))

def frame_show():
    """显示程序主体"""
    frame = MyFrame()
    frame.menu_bar()
    frame.form_sizer()
    frame.Show()