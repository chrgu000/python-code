# -*- coding: utf-8 -*-
'''
GUI之Tkinter
'''
from tkinter import *
import sys, turtle, tkinter.messagebox, codecs

"""疯狂的python，网易云课堂演示
root = Tk()  # 生成主窗口

'''添加菜单'''
menu = Menu(root)  # 生成菜单
submenu  = Menu(menu, tearoff = 0)  # 生成下拉菜单
submenu.add_command(label='Open',command = menuExit)  # 下拉菜单open
submenu.add_command(label='Save')  # 下拉菜单open
menu.add_cascade(label="File", menu = submenu) # 将下拉菜单添加到菜单
root.config(menu = menu )  # 将菜单项添加到root GUI窗口

'''添加标签'''
label = Label(root, text = '你好！') # 生成标签
label.pack()  # 将标签添加到主窗口

'''添加按钮1'''
button1 = Button(root, text = '五角星') # 生成按钮
button1.pack()

'''按键1事件'''
def wjx(event):  # 事件函数
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)

button1.bind('<Button-1>', wjx) # 绑定wjx事件到迎按钮button1,响应方式为<Button-1>(鼠标左键)

root.mainloop()  # 进入消息循环（GUI交互）
"""


'''练习''' # 代码思路不对，需要修改
errorInfo = '''
+--------------------------------+
|             FAILD              |
 --------------------------------
|                                |
\t%s
+--------------------------------+'''
dyadicList = ['user_info', 'user_deleted']  #二维列表文件

def openFiles(filepath,permission='a+', cod= 'utf-8'):   #读取文件信息到列表
    f = codecs.open(filepath,permission,cod)
    f.seek(0,)
    infoList = f.readlines()
    for x in range(len(infoList)):
        if filepath in dyadicList:
                #二维列表需要去掉换行符并用eval转换成List
            infoList[x] = eval(infoList[x].strip('\n'))
        else:
            infoList[x] = infoList[x].strip('\n')  #一维列表直接去掉末尾的换行符即可
    return f, infoList
##加载文件信息开始
fileUserInfo, userInfoList = openFiles('user_info')
fileUserDeleted, userDeletedList = openFiles('user_deleted')

class WindowsStyle:
    '''窗口各种样式设置'''
    def buttonStyle1(self, parent, name, w=15, h=2, command=''):
        '''按钮样式1'''
        self.button = Button(parent, text=name, width=w, height=h, command=command)
        return self.button

    def buttonStyle2(self, parent, name, w=15, h=1, command=''):
        '''按钮样式2'''
        self.button = Button(parent, text=name, width=w, height=h)
        return self.button


class MainWindows:
    '''主界面'''


    ######################################事件
    def menuHomeButton1Evt(self, evt):
        self.menuQuery(self.frm1)
        self.textArea('')

    def menuHomeButton2Evt(self, evt):
        #self.menuChange(self.frm1)
        #self.textArea('')
        self.frm('').hide()

    def userNameAll(self, event):
        self.msg = ''
        if len(userInfoList) > 0:
            for x in userInfoList:
                self.msg = self.msg + x[0] + '   '
        else:
            self.msg = '当前没有任何用户'
        self.textArea("所有用户名单：\n\n"+self.msg)

    def userInfoAll(self, event):
        self.msg = ''
        if len(userInfoList) > 0:
            for x in userInfoList:
                self.msg = self.msg + ('姓名：%s\t性别：%s\t年龄：%s\t城市：%s\n' % (x[0], x[1], x[2], x[3]))
        else:
            self.msg = '当前没有任何用户'
        self.textArea("用户详细信息:\n\n"+self.msg)

    def adultMan(self, event):
        self.msg = ''
        someone = 'no'
        for x in userInfoList:
            if x[2] >= 18:
                self.msg = self.msg + x[0] + '  '
                someone = 'yes'
        if someone == 'no':
            self.msg = '没有符合条件的用户'
        self.textArea("成年用户:\n\n"+self.msg)

    def youngMan(self, event):
        self.textArea("未成年用户")
    def userDeleted(self, event):
        self.textArea("已删除用户")

    def userAdd(self):

        self.v = IntVar()
        self.v.set(1)
        self.user_add = Tk()
        self.user_add.title("添加用户")

        self.frm_user_add = Frame(self.user_add, width=50)
        self.frm_user_add.grid(padx=10, pady=10)

        self.label_name = Label(self.frm_user_add, text='姓名：', fg='blue', font="微软雅黑 12 bold")
        self.label_gender = Label(self.frm_user_add, text='性别：', fg='blue', font="微软雅黑 12 bold")
        self.label_age = Label(self.frm_user_add, text='年龄：', fg='blue', font="微软雅黑 12 bold")
        self.label_city = Label(self.frm_user_add, text='城市：', fg='blue', font="微软雅黑 12 bold")

        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.label_gender.grid(row=1, column=0, padx=5, pady=5)
        self.label_age.grid(row=2, column=0, padx=5, pady=5)
        self.label_city.grid(row=3, column=0, padx=5, pady=5)

        self.entry_name = Entry(self.frm_user_add, width=15)
        #self.entry_gender = Entry(self.frm_user_add, width=15)
        self.radiobutton_gender1 = Radiobutton(self.frm_user_add, text="男", value=1 , variable=self.v)
        self.radiobutton_gender2 = Radiobutton(self.frm_user_add, text="女", value=2 , variable=self.v)
        self.entry_age = Entry(self.frm_user_add, width=15)
        self.entry_city = Entry(self.frm_user_add, width=15)

        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        #self.entry_gender.grid(row=1, column=1, padx=5, pady=5)
        self.radiobutton_gender1.grid(row=1, column=1, padx=5, pady=5, sticky="W")
        self.radiobutton_gender2.grid(row=1, column=1, padx=5, pady=5, sticky="E")
        self.entry_age.grid(row=2, column=1, padx=5, pady=5)
        self.entry_city.grid(row=3, column=1, padx=5, pady=5)

        self.button_ok = Button(self.frm_user_add, text='OK', width=8)
        self.button_cancle = Button(self.frm_user_add, text='Cancle', width=8)

        self.button_ok.grid(row=5,column=0, padx=5, pady=5)
        self.button_cancle.grid(row=5,column=1, padx=5, pady=5)

        self.user_add.mainloop()

        self.user_info = [self.entry_name, self.v.get(), self.entry_age, self.entry_city]
        return self.user_info

    ##########控件
    def frm(self, parent):
        self.frm = Frame(parent, bg='red')
        self.frm.grid(row=0, column=0)

        def hide(self):
            self.frm.grid_forget()

    def frm1(self, parent):
        self.frm1 = Frame(parent, bg='blue')
        self.frm1.grid(row=1, column=0)
        self.frm1.grid_forget()

    def menuHome(self, parent):
        '''主菜单'''

        self.bs = WindowsStyle()

        self.button1 = self.bs.buttonStyle1(parent,  "用户信息查看")
        self.button2 = self.bs.buttonStyle1(parent,  "用户信息增改删")
        self.button3 = self.bs.buttonStyle1(parent,  "保存")

        self.button1.grid(row=0, column=0, padx=5, pady=5)
        self.button2.grid(row=0, column=1, padx=5, pady=5)
        self.button3.grid(row=0, column=2, padx=5, pady=5)

        self.button1.bind("<ButtonRelease-1>", self.menuHomeButton1Evt)
        self.button2.bind("<ButtonRelease-1>", self.menuHomeButton2Evt)


    def menuQuery(self, parent):
        '''查询菜单'''
        self.bs = WindowsStyle()

        self.button1 = self.bs.buttonStyle2(parent,  "所有用户姓名")
        self.button2 = self.bs.buttonStyle2(parent,  "用户详细信息")
        self.button3 = self.bs.buttonStyle2(parent,  "成年用户")
        self.button4 = self.bs.buttonStyle2(parent,  "未成年用户")
        self.button5 = self.bs.buttonStyle2(parent,  "已删除用户")
        #self.button6 = self.bs.buttonStyle2(parent,  "返回")

        self.button1.grid(row=0, column=0, padx=5, pady=5)
        self.button2.grid(row=0, column=1, padx=5, pady=5)
        self.button3.grid(row=0, column=2, padx=5, pady=5)
        self.button4.grid(row=1, column=0, padx=5, pady=5)
        self.button5.grid(row=1, column=1, padx=5, pady=5)
        #self.button6.grid(row=1, column=2, padx=5, pady=5)

        self.button1.bind("<ButtonRelease-1>",self.userNameAll)
        self.button2.bind("<ButtonRelease-1>",self.userInfoAll)
        self.button3.bind("<ButtonRelease-1>",self.adultMan)
        self.button4.bind("<ButtonRelease-1>",self.youngMan)
        self.button5.bind("<ButtonRelease-1>",self.userDeleted)

    def menuChange(self, parent):
        '''查询菜单'''
        self.bs = WindowsStyle()

        self.button1 = self.bs.buttonStyle2(parent,  "添加用户")
        self.button2 = self.bs.buttonStyle2(parent,  "修改用户信息")
        self.button3 = self.bs.buttonStyle2(parent,  "删除用户",)
        #self.button4 = self.bs.buttonStyle2(parent,  "返回",)

        self.button1.grid(row=0, column=0, padx=5, pady=5)
        self.button2.grid(row=0, column=1, padx=5, pady=5)
        self.button3.grid(row=0, column=2, padx=5, pady=5)
        #self.button4.grid(row=1, column=0, padx=5, pady=5)

        self.button1.bind("<ButtonRelease-1>", self.userAdd)

    def textArea(self,  word, w=50, h=20):
        self.t = Text(  width=w, height=h)
        self.t.insert('1.0', word)
        self.t.grid(row=9, column=0, padx=5, pady=5)

    def frms(self):
        pass

    def __init__(self):   # 开始初始化界面

        self.root = Tk()   # 初始化窗口

        '''开始设置窗口属性'''
        self.root.title("用户信息管理系统")   # 窗口标题
        #self.root.geometry("800x600")   # 窗口大小，是x，不是*
        #self.root.resizable(width=False, height=True)  # 窗口宽高是(True)否(False)可变，默认为True
        '''窗口属性设置完毕'''

        '''开始添加菜单'''
        self.menu = Menu(self.root)  # 生成菜单
        #self.submenu = Menu(self.menu, tearoff = 0) # 生成下拉菜单
        #self.submenu.add_command(label = "exit", command = self.root.destroy) # 将菜单项exit添加到下拉菜单
        #self.menu.add_cascade(label = "File", menu = self.submenu) # 将下拉菜单添加到菜单
        self.menu.add_cascade(label = "Exit", command='exit')
        self.root.config(menu = self.menu ) # 配置菜单到窗口
        '''菜单添加完毕'''

        self.frm(self.root)
        self.frm1(self.root)

        self.menuChange(self.frm)
        #self.menuChange(self.frm1)
        print(__name__)
        #self.textArea('')
        l = self.userAdd()
        print(l)
        self.root.mainloop()   # 进入消息循环


s = MainWindows()
