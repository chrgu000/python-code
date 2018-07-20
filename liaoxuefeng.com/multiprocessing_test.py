#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
关于多进程
"""
from multiprocessing import Pool
import os, time, random

if os.name ==  'posix': # Unix/Linux/Mac
    print('Process (%s) start...' % os.getpid())
    #一个工作在Unix/Linux/Mac:
    pid = os.fork()
    if pid == 0:
        print('我是子进程 （%s）, 我的父进程是(%s)' % (os.getpid(), os.getppid()))
    else:
        print('我（%s）创建了一个子进程（%s）.' % (os.getpid(), pid))
elif os.name == 'nt': # win
    from multiprocessing import Process


    def run_proc(name):
        """子进程要自执行的代码"""
        print('运行子进程 %s (%s)...' % (name, os.getpid()))

    if __name__ == '__main__1':
        print('父进程 %s。' % os.getpid())
        p = Process(target=run_proc, args=('test',))
        print('子进程启动。 ')
        p.start()
        p.join()
        print('子进程结束。')

    #Pool, 如果要启动大量的子进程，用进程池方式批量创建子进程
    def long_time_task(name):
        """子进程代码"""
        print("运行进程 %s (%s)" % (name, os.getpid()))
        start = time.time()
        time.sleep(random.random()*3) # 暂停
        end = time.time()
        print("进程 %s 运行了 %0.2f 秒。" % (name, end - start))

    if __name__ == '__main__':
        print("父进程 %s。" % os.getpid())
        p = Pool(4) # 进程池大小，默认CPU核数
        for i in range(5):
            p.apply_async(long_time_task, args=(i,))
        print("等待所有进程完成...")
        p.close()
        p.join()
        print("所有子进程已经完成。")