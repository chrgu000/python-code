#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
"""

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    """写数据的进程"""
    print("写入的进程： %s" % os.getpid())
    for value in ['A', 'B', 'C']:
        print("把 %s 加入queue..." % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    """读数据的进程"""
    print("读取的进程： %s " % os.getpid())
    while True:
        value = q.get(True)
        print("从queue中读取 %s" % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw,写入
    pw.start()
    # 启动子进程pr,读取
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环， 无法等待其结束，只能强行终止：
    pr.terminate()