#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author: WangBai
#Date: 2018-7-4 14:12
"""
多线程的学习:
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。

启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
"""

import time, threading


def loop():
    """新线程执行的代码"""
    print("线程 %s 现在开始运行……" % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("线程 %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("线程 %s 结束。" % threading.current_thread().name)

if '多线程的初级演示' == False:
    print("线程 %s 开始运行……" % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print("线程 %s 结束。" % threading.current_thread().name)

# 多进程间，变量不共用； 多线程间，变量共用
# 多个线程操作一个变量会把内容改乱：
# 要确保多线程不会同时操作变量，加锁 threading.Lock()
balance = 0 # 银行存款
lock = threading.Lock()

def change_it(n):
    """先存后取， 结果应该为0"""
    global balance
    balance += n
    balance -= n

def run_thread(n):
    """线程要进行的操作"""
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完了要释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
