#!/usr/bin/env pytho3
# -*- coding: utf-8 -*-

import psutil  # 获取系统信息模块，CPU、内存、磁盘的使用情况
import time
import datetime


def monitor_system():
    # 获取CPU使用情况
    cpuper = psutil.cpu_percent()
    # 获取内存使用情况：系统内存大小，使用内存，有效内存，内存使用率
    mem = psutil.virtual_memory()
    # 内存使用率
    memper = mem.percent
    # 获取当前时间
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} cpu:{cpuper}%, mem:{memper}%'
    print(line)

def loop_monitor():
    while True:
        monitor_system()
        # 2s检查一次
        time.sleep(3)

loop_monitor()
