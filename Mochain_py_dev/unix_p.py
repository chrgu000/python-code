#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ssh登录Linux服务器，执行shell命令
"""

import paramiko
import json
import sys
import threading



class Server:
    """连接服务器执行命令操作"""

    def __init__(self, host, port, username, passwd, cmd):
        """初始化属性"""
        self.host = host
        self.port = port
        self.username = username
        self.passwd = passwd
        self.cmd = cmd

    def connect_server(self):
        """连接服务器"""

        # 建立一个sshclient对象
        self.ssh = paramiko.SSHClient()
        # 设置成默认自动接受密钥，此方法必须放在conect方法的前面
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            # 连接服务器，超时时间为30s
            self.ssh.connect(host, port, username, passwd, timeout=30)
        except:
            self.ssh.close()
            print("Connect to %s Faild." % self.host)

    def run_cmd(self):

        for m in self.cmd:
            # windows下换行为\r\n,Linux下为\n，需处理
            m = m.strip()
            # 执行命令，结果放到stdout中，错误放到stderr
            try:
            	stdin, stdout, stderr = self.ssh.exec_command(m)
            	for outline in stdout:
            		print(outline.strip())
            	for errline in stderr:
            		print(errline.strip())
            except Exception as e:
           		print("execute command %s error, error message is %s" % (m, e))

        print("%s\tFinished!\n" % self.host)

        # 关闭连接
        #self.ssh.close()

    def send_cmd(self):
    	"""交互式命令操作"""
    	chan = self.ssh.invoke_shell()
    	chan.send('screen -S ')

    	for c in cmd:
    		chan.send(c)
    		out=chan.recv(1024)
    		for o in out:
    			print(o.strip())


    def upload_file(self):
        """上传单个文件到服务器"""
        t = paramiko.Transport((self.host, self.port))
        t.connect(username=self.username, password=self.passwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put("lnmp1.5.tar.gz", "lnmp1.5.tar.gz")
        t.close()


def load_datas(file):
    """读取列表文件"""
    try:
        with open(file, 'r') as f:
            file_data = f.readlines()
            # IP列表需要把每行生成一个新的list
            if 'ip' in file:
                for i, v in enumerate(file_data):
                    # 去掉空格、回车，生成新的list
                    file_data[i] = list(v.strip().split(','))
            return file_data
    except:
        print('Please check file: %s' % file)
        exit()


def run_steps(host, port, username, passwd, cmd):
    """部署过程"""
    cs = Server(host, port, username, passwd, cmd)
    cs.connect_server()  # 连接服务器
    #cs.upload_file()  # 上传文件
    #cs.run_cmd()  # 执行命令
    cs.send_cmd()

if __name__ == '__main__':

    """host = '192.168.50.128'
    port = 22
    username = 'root'
    passwd = 'wodemima'"""

    cmd = load_datas('cmd.txt')
    hosts = load_datas('ip_list.txt')

    for i in range(len(hosts)):
        print("开始执行任务………………")
        host, port, username, passwd = hosts[i]

        t = threading.Thread(target=run_steps, args=(
            host, int(port), username, passwd, cmd))
        t.start()