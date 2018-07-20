#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-04-13 16:00:46
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
列表窗口
"""

class ListBoxFrame(wx.Frame):
    """列表窗口"""
    def __init__(self):
        """初始化属性"""

        self.data_list = []  # 存放上一次的数据

