# /usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Bing


"""
服务器执行命令输出信息窗口

"""

import sys
import wx
import threading
from server import Server

class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None,
                          title="wxPython Redirect Tutorial")

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL
        log = wx.TextCtrl(panel, wx.ID_ANY, size=(300,100),
                          style=style)
        btn = wx.Button(panel, wx.ID_ANY, 'Push me!')
        self.Bind(wx.EVT_BUTTON, self.onButton, btn)

        # Add widgets to a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(log, 1, wx.ALL|wx.EXPAND, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

        # redirect text here
        sys.stdout=log

    def my_program(self):
        my_server = Server('172.16.175.128', 22, 'wodemima')
        my_server.exec_cmd('yum -y cmake')
    def onButton(self, event):
        #print("You pressed the button!")
        log_thread = threading.Thread(target=self.my_program)
        log_thread.start()


# Run the program
if __name__ == "__main__":
    def my_app():
        app = wx.App(False)
        frame = MyForm().Show()
        app.MainLoop()
    app_thread = threading.Thread(target=my_app)
    app_thread.start()
    #app_thread.join()