# -*- coding: utf-8 -*-
'''
GUI之wxPython
'''
import huatu  # 导入写好的绘制美国国旗的文件
import wx, turtle

class Frame(wx.Frame):  # 继承内置Frame方法
    pass


class MyApp(wx.App):   # 继承默认wx.App类
    def OnInit(self):  # 内置初始化方法
        self.frame = Frame(parent=None,
                            title="wx学习",
                            size=(400, 300),
                            pos=(400, 320)
                            ) # 框架
        panel = wx.Panel(self.frame, -1)  # 创建面板
        self.button_wjx = wx.Button(panel,
                                    -1,
                                    "五角星",
                                    size=(90,30),
                                    pos=(10, 10)
                                    )
        self.button_flagUSA = wx.Button(panel,
                                     0,
                                     "USA国旗",
                                     size=(90,30),
                                     pos=(99, 39)
                                    )

        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.evtButtonFlagUSA, self.button_flagUSA)
        self.Bind(wx.EVT_BUTTON, self.evtButtonWJX, self.button_wjx)


        self.frame.Show()  # 显示框架
        self.SetTopWindow(self.frame)

        return True  # 必须返回一个真值

    def evtButtonFlagUSA(self, evt):
        self.fu = huatu.Flag()
        self.fu.USA()

    def evtButtonWJX(self, evt):
        self.fw = huatu.Flag()
        self.fw.wjx(90)
        turtle.mainloop()


if __name__ == '__main__':
    print(__doc__)
    app = MyApp()  # 应用程序对象
    app.MainLoop()  # 进入消息循环（注意MainLoop 大小写）

