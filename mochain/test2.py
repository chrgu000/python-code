"""from pexpect import pxssh
import sys

s = pxssh.pxssh()
#s.logfile = sys.stdout
hostname = '10.0.0.14'
username = 'root'
password = '0'
print(type(s))
print(hostname == b'10.0.0.14')
#s.login(hostname,username)
s.sendline('ls /')
s.prompt()  #匹配系统提示符
s.sendline('whoami')
s.prompt()
s.logout()"""


import threading
import time

sem=threading.Semaphore(4)  #限制线程的最大数量为4个

def gothread():
    with  sem:  #锁定线程的最大数量
        for i in range(8):
            print(threading.current_thread().name,i)
            time.sleep(1)

for i in range(5):
    threading.Thread(target=gothread).start()