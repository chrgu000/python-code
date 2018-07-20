    #!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

def findDirFile(dirName, keyword):
    #os.chdir(dirName)
    for x in os.listdir(dirName):
        if os.path.isdir(x) and x[0] != '.':
            nextDirName = os.path.realpath(x)
            print(x, nextDirName)
            findDirFile(nextDirName, keyword)
        if os.path.isfile(dirName + '/' + x) and (keyword in x):
            print('找到以下文件：%s' % os.path.realpath(x))

homepath = r'c:\users\dawang\python-code'
findDirFile(homepath, '00')