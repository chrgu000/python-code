 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
电费计算的方法
"""
import codecs
import wx
import json
import datetime

def file_read():
    """读取文件"""
    try:  # 如果文件不存在
        with open('dianfei.json') as f:
            # 加载json
            l = json.load(f)
    except :
        l = []  # 文件不存在返回空表
    return l

def file_write(data_list):
    """保存文件，覆盖或者追加"""
    if isinstance(data_list[0], list):
        """覆盖文件"""
        l = data_list
    else:
        """向文件尾部添加内容"""
        l = file_read()
        l.append(data_list)
    # 数组排序
    l = sorted(l, key =lambda l:l[0])  # 二维列表用第个按第0列排序
    with open('dianfei.json', 'w') as f:
        # 制作json文件，保持原编码
        json.dump(l, f, ensure_ascii=False)

def clear_all_datas(parent):
    #retCode = wx.MessageBox("此操作将删除所有数据，谨慎操作！", "WARNING",
    #            style=wx.YES_NO)
    dialog = wx.TextEntryDialog(parent,
            "此操作将删除所有数据，谨慎操作！\n确认请输入：delete",
            "警告", "", style=wx.OK|wx.CANCEL)
    if dialog.ShowModal() == wx.ID_OK:
        #print("You entered: %s" % dialog.GetValue())
        #wx.MessageBox("你输入了：%s" % dialog.GetValue())
        if dialog.GetValue() == "delete":
            with open('dianfei.json', 'w') as f:
                wx.MessageBox("数据清除成功")

def my_font(size, faceName):
    """设置字体"""
    font = wx.Font(size, wx.DEFAULT, wx.NORMAL, wx.NORMAL,
                False, faceName)
    return font

def creat_TextCtrl(parent, label, style):
    """创建一个文本输入框"""
    if style == 1:
        size=(80,25)
        style=0
    elif style == 2:
        size=(90,35)
        style=wx.TE_READONLY|wx.TE_CENTER
    text = wx.TextCtrl(parent, -1, label,  size=size, style=style)
    return text

def creat_StaticText(parent, label):
    """创建一个静态文本显示框"""
    text = wx.StaticText(parent, -1, label)

    return text

def creat_button(parent, label, size=(-1, -1)):
    """创建一个按钮"""
    button = wx.Button(parent, -1, label, size=size)
    return button

def creat_BoxSizer(parent, label, widget):
    """创建一个BoxSizer"""
    box = wx.StaticBox(parent, -1, label)
    box_sizer = wx.StaticBoxSizer(box, wx.VERTICAL)
    box_sizer.Add(widget)

    return box_sizer

def check_data_files(text_show, button):
    """
    检查是否存在历史数据
    没有的话提示先录入
    """
    try:
        with open('dianfei.json', 'r') as f:
            button.Enable()
        file_read()[-1]
    except:
        text_show.SetValue("Erro:\n\
                    至少需要一条历史数据，填写后点击 保存数据")
        retCode = wx.MessageBox(
                    "\t至少需要一条历史数据\n\t填写后点击 保存数据", "Error")
        button.Disable()

def check_data_type(widgets):
    """检查数据格式"""
    for widget in widgets[1:8]:
        try:
            int(widget.GetValue())
        except :
            # 计算、保存按钮不可用
            widgets[11].Enable(False)
            widgets[12].Enable(False)
            # 报错并定位到错误位置
            wx.MessageBox("电数全部都应该是数字且不为空!", "格式错误")
            widget.SetFocus()  # 设置当前为焦点
            #widget.SetValue("0")  # 值重设为0
            widget.SetSelection(-1,-1)  # 选定从0到-1范围的字符
            #widget.SetInsertionPointEnd()  # 光标移动到最后
            return False

    widgets[11].Enable(True)  # 计算按钮可用
    #widgets[12].Enable(True)  # 保存按钮可用

    return True

    '''if not(widgets[0].HasFocus()):
        """日期输入框失去焦点后检查正确性"""
        check_date(widgets)'''

def money_count(widgets, text_show):
    """计算金额"""
    money = 0
    for x in range(5, 9):
        money += int(widgets[x].GetValue()) * 1.3
    money = int(money)
    #print("money", money)
    widgets[9].SetLabel(str(money))

    update_saveBtn(widgets)

def count_msg(widgets, text_show):
    """计算结果显示到文本显示区"""
    pass

def check_date(widgets):
    """检查当前日期是否是新日期"""
    date = widgets[0].GetValue()
    # 检查日期格式
    try:
        """检测日期"""
        datetime.date(int(date[:4]),int(date[4:6]),int(date[6:]))
    except:
        wx.MessageBox("请输入正确的日期", "日期出错了")
        widgets[0].SetFocus()
        #widget.SetInsertionPointEnd()  # 光标移动到最后
        widgets[0].SetSelection(0,-1)  # 选定从0到-1范围的字符

    """if int(widget.GetValue()) < file_read()[-1][0]:
        return True
    else:
        return False"""

def getDays(date_min, date_max):
    """计算两个日期相差的天数"""
    try:
        """将日期转换为字符串"""
        date_min = str(date_min)
        date_max = str(date_max)
    except TypeError:
        """出错的格式已经正确"""
        pass

    d1 = datetime.date(int(date_min[:4]),int(date_min[4:6]),int(date_min[6:]))
    d2 = datetime.date(int(date_max[:4]),int(date_max[4:6]),int(date_max[6:]))
    interval_days = (d2-d1).days
    return interval_days


def getValue(widgets, text_show):
    """得到余电及充值的数据"""
    widgets = widgets[:10]  # 仅读取前10个窗口部件的值
    vl =[]
    for widget in widgets:
        if isinstance(widget, wx._core.StaticText):
            vl.append(int(widget.GetLabel()))  # 静态文本取徝
        else:
            vl.append(int(widget.GetValue()))
    return vl

def save_data(widgets, results, text_show):
    """保存数据到文件"""

    text_show.Clear()  # 清除文本显示区内容
    msg_list = ["日期：",
            "506#余电：", "507#余电：",
            "508#余电：", "509#余电：",]
    for x in range(5):
        text_show.AppendText(msg_list[x]+str(results[x]))
        if x != 0:
            text_show.AppendText("   充值："+str(results[x+4]))
        text_show.AppendText("\n")

    # 确认是否保存数据
    retCode = wx.MessageBox("是否继续？", "WARNING",style=wx.YES_NO)
        #print("retCode:",retCode, type(retCode))
    if retCode == 2:
        file_write(results)
        # 保存提示成功后文本框归零
        text_show.AppendText("添加成功！！！")
        for x in widgets[1:9]:
            x.SetValue('0')
    else:
        text_show.SetValue("取消保存！")

def get_averages(data_last, data_now, interval_days):
    """计算平均数"""
    # 间隔天数为0时（当天），改为1
    if not interval_days:
        interval_days = 1
    if data_last == data_now:
        data_now = [x*0 for x in range(len(data_now))]
    averages = []
    for x in range(1, 5):
        average = round((data_last[x] + data_last[x+4] - data_now[x]) /
                        interval_days, 2)
        averages.append(average)
    return averages

def data_count(widgets, text_show):
    """数据计算"""
    text_show.Clear()
    # 取得历史最后一条数据
    data_last = file_read()[-1]
    # 取得当前填写数据
    data_now = getValue(widgets, text_show)

    # 老日期只计算金额
    if int(widgets[0].GetValue()) < data_last[0]:
        # 计算金额
        money = int((data_now[5] + data_now[5] + data_now[5] + data_now[5])
                    * 1.3)
        # 将金额填充到控件
        widgets[9].SetLabel(str(money))
        # 文本显示框显示提示信息
        text_show.SetValue("当前日期：%s 早于历史最后一次日期：%s\n\
                        请填写完整,计算金额后保存数据".replace('    ', '')
                        % (widgets[0].GetValue(), data_last[0]))
        if not money:
            text_show.SetValue("WaSaiHey，你好歹输入下数据吧！")
        #return
    else:
        # 得到本次和最后一次充电的相隔天数
        date_old = data_last[0]
        date_now = widgets[0].GetValue()
        interval_days = getDays(date_old, date_now)

        # 平均每天耗电数
        averages = get_averages(data_last, data_now, interval_days)

        # 计算减去余电后期许天数需要充值的电数
        days = int(widgets[10].GetValue())  # 期许天数
        deposits = []  # 存放充值数
        deposits_sum = 0  # 计算充值总和
        for x in range(4):
            # 单个充值度数
            deposit = int(round(averages[x] * days -
                        int(widgets[x+1].GetValue()), -2))
            #deposit = int(round(averages[x] * interval_days, -2))

            deposits_sum += deposit
            deposits.append(deposit)

        # 计算金额，单价为1.3元/度
        money = int(deposits_sum*1.3)  # 金额
        deposits.append(money)

        # 将值写入充值框
        for x in range(5):
            if deposits[x] < 0:
                deposits[x] = 0
            if x == 4:
                widgets[x+5].SetLabel(str(deposits[x]))
            else:
                widgets[x+5].SetValue(str(deposits[x]))

        msg = ["本次抄表日期：", "506#余电：", "507#余电：", "508#余电：", "509#余电："]
        for x in range(5):
            text_show.AppendText(msg[x]+str(widgets[x].GetValue()))
            if x == 0 :
                text_show.AppendText(
                            "\n上次充值日期：%s, 已使用%s天, 期许使用%s天\n" %
                            (data_last[0], interval_days, days)
                                    )
            else:
                text_show.AppendText("  平均：%s,  充值：%s \n" %
                            (averages[x-1], deposits[x-1]))

        text_show.AppendText("\n总计金额：%s元" % deposits[-1])

        update_saveBtn(widgets)

def update_saveBtn(widgets):
    """更新数据保存按钮是否可用"""
    if int(widgets[9].GetLabel()) > 0:
        widgets[12].Enable(True)
    else:
        widgets[12].Enable(False)

def all_dates(text_show):
    """获取所有充值的日期，并在text_show区域显示"""

    datas = file_read()
    if datas:
        text_show.SetValue("共计%d条充值记录：\n\n" % len(datas))
        n = 0
        # 生成需要改变字体颜色的位置点
        pos = [h for j in ((x, x+1) for x in range(-1,20,4)) for h in j]
        for data in datas:
            date_str = str(data[0])[:4] + "年" + \
                    str(data[0])[4:6] + "月" + \
                    str(data[0])[6:] + "日"
            text_show.AppendText("日期：" + date_str)
            if n % 2 != 0:
                text_show.AppendText("\n")
            else:
                text_show.AppendText("\t")
            if n in pos:

                text_show.SetStyle(11+15*n, 11+15*n+14,
                            wx.TextAttr("black","green"))

            n += 1

def history_btn(text_show):
    """历史数据"""
    msg = ["日期：", "506#：", "507#：", "508#：", "509#：",
                    "506#充值：", "507#充值：", "508#充值：", "509#充值："]
    dianfei_list = file_read()
    #print(dianfei_list)
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
        text_show.AppendText("""
            +----------------------+
            |--{}{:^10}--|
            |------------------------|
            | 表箱 |   余电  |  充值 |
             {}{:^6}{:^8}
             {}{:^6}{:^8}
             {}{:^6}{:^8}
             {}{:^6}{:^8}
            """.format(msg[0],x[0],
                    msg[1],x[1],x[5],
                    msg[2],x[2],x[6],
                    msg[3],x[3],x[7],
                    msg[4],x[4],x[8]).replace(" "*12, ""))


def datas_sizer(scroll, data_lists, scroll_focus):
    """返回已存数据信息的布局和控件列表"""
    if not data_lists:
        pass  # 没有数据直接退出

    # 用于存放所有的控件
    widgets = []
    #data_lists = file_read()
    #data_lists.reverse()  # 倒序

    # 整体布局
    scroll_sizer = wx.BoxSizer(wx.VERTICAL)

    for data_list in data_lists:

        # 创建布局
        sizer = wx.GridBagSizer(hgap=0, vgap=0)
        list_index = data_lists.index(data_list)
        # 相隔天数和平均值
        if list_index+1 < len(data_lists):
            interval_days = getDays(data_lists[list_index+1][0],
                                            data_list[0])

            list_index += 1
        else:
            interval_days = 30

        averages = get_averages(data_lists[list_index],
                                    data_list,
                                    interval_days)

        # 标题及在布局内对应的pos
        titles = {"日期":(0,0),
                "表箱":(1,0),
                "余电":(2,0),
                "充值":(3,0),
                "平均":(4,0),
                "506号":(1,1),
                "507号":(1,2),
                "508号":(1,3),
                "509号":(1,4),
                }

        # 将标题放到相应的pos
        for key,value in titles.items():
            if key == "日期":
                key = "%s年%s月%s日" % (str(data_list[0])[:4],
                                        str(data_list[0])[4:6],
                                        str(data_list[0])[6:],
                                        )
                span=(1,5)
                #display_datas[key] = data_list
            elif key == "平均":
                key = "%s天均值" % interval_days
            else:
                key = key
                span=(1,1)
            #print("df_key: ", key)
            text = creat_TextCtrl(scroll, key, 2)
            # 颜色和字体
            text.SetFont(my_font(15, '微软雅黑'))
            #text.SetBackgroundColour('yellow')

            if "年" in key:
                scroll_focus.append(text)

            # 设置丰富样式的文本
            if key == "日期":
                text.SetStyle(1, 3, wx.TextAttr("white", "black",))

            # 控件添加到列表和布局中
            widgets.append(text)
            sizer.Add(text, pos=value, span=span, flag=wx.EXPAND)

        # 将数据放到相应pos上
        for row in range(3):
            for col in range(1, 5):
                if row < 2:
                    index = row*4+col
                    label = str(data_list[index])
                else:
                    label = str(averages[col-1])
                text = creat_TextCtrl(scroll, label,
                        2)
                # 颜色和字体
                text.SetFont(my_font(14, ''))
                widgets.append(text)
                sizer.Add(text, pos=(row+2, col))  # 加入布局

        # 统计数据
        num_count = data_list[5]+data_list[6]+data_list[7]+data_list[8]  #总和
        days = int((data_list[3] + data_list[7]) / averages[2])  # 可使用天数
        data_count_text = "注：合计充值%s度，单价:%s元，共%s元。可使用%s天。"\
                        % (
                            num_count,
                            data_list[-1]/num_count,
                            data_list[-1],
                            days,
                        )
        count_text = creat_TextCtrl(scroll, data_count_text,
                                            2)
        count_text.SetFont(my_font(12, ''))
        sizer.Add(count_text, pos=(5,0), span=(1,5), flag=wx.EXPAND)
        scroll_focus.append(count_text)

        # 最后的列和行可扩展
        sizer.AddGrowableRow(5)
        sizer.AddGrowableCol(4)

        scroll_sizer.Add(sizer, 0, wx.ALL|wx.ALIGN_CENTER, 15)

    # 返回布局和按顺序的控件列表
    return scroll_sizer, widgets

def del_data_btn(parent, listBox, scroll, scroll_sizer, scroll_focus, data_lists):
    """删除数据按钮"""
    index = listBox.GetSelection()
    print("index:", index)
    if index != -1:
        dialog = wx.TextEntryDialog(parent,
            "此操作将删除%s的数据，谨慎操作！\n确认请输入：delete" \
            % listBox.GetStringSelection(),
            "警告", "", style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK and dialog.GetValue() == "delete":
            #print("You entered: %s" % dialog.GetValue())
            #wx.MessageBox("你输入了：%s" % dialog.GetValue())

            listBox.Delete(index)

            #print("1111", len(scroll_sizer.GetChildren()),
            #        len(scroll_focus))
            # 隐藏选择列表对应的数据
            scroll_sizer.GetItem(index).Show(False)
            # 删除选择后的焦点跳转
            for x in range(2):
                scroll_focus.pop(index*2)
            # 重新布局数据显示
            scroll.Scroll(1, 1)  # 滚动到像素位置
            scroll_sizer.Layout()

            # 保存修改到文件
            data_lists.pop(index)
            file_write(data_lists)

    else:
        wx.MessageBox("请选择要删除的数据", "WARNING")

def creat_listBox_label(data_lists):
    """将数据生成为一个字典"""
    scroll_focus = []
    for data_list in data_lists:
        date = "%s年%s月%s日" % (str(data_list[0])[:4],
                                str(data_list[0])[4:6],
                                str(data_list[0])[6:],
                                )
        scroll_focus.append(date)

    return scroll_focus