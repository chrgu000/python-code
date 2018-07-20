#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-04-24 14:43:50
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
打印的类
"""

import os
import wx


FONTSIZE = 10

class TextDocPrintout(wx.Printout):
    """调用系统打印机"""
    def __init__(self, text, title, margins):
        """初始化"""

        wx.Printout.__init__(self, title)
        self.lines = text.split('\n')
        self.margins = margins

    def HasPage(self, page):
        return page <= self.numPages

    def GetPageInfo(self):
        return (1, self.numPages, 1, self.numPages)