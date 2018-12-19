#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#author: xiaobing

"""
conncet remote Linux server:
    exec commad
    upload file
"""
import paramiko


class Server:
    """连接服务器执行命令操作"""

    def __init__(self, host, port, password, username='root'):
        """初始化属性"""
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        # 连接到服务器
        self.connect_server()

    def connect_server(self):
        """连接服务器"""

        # 建立一个sshclient对象
        self.ssh = paramiko.SSHClient()
        # 设置成默认自动接受密钥，此方法必须放在conect方法的前面
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            # 连接服务器，超时时间为30s
            print("Now connect to server [%s]" % self.host)
            self.ssh.connect(self.host, self.port,
                             self.username, self.password, timeout=30)
        except Exception as e:

            #if e in "Authentication failed":
            #    print("Username or Password Error !!")
            #elif e in "Unable to connect to port":
            #    print("Port Error.")
            #elif e in "time out":
            #    print("Timeout!!\nCheck 【HostIp】 or 【Server Power】 or 【Server`s firewall】 !!")
            print("Connect to %s@%s:%s Faild." % (self.username, self.host, self.port))
            self.ssh.close()
            exit()

    def exec_cmd(self, cmd):
        """执行单条的命令"""
        out = ''  # 用来判断是否有正常输入信息
        # windows下换行为\r\n,Linux下为\n，需处理
        cmd = cmd.strip()
        # 执行命令，结果放到stdout中，错误放到stderr
        try:
            print('\n【 %s 】 Exec_command: "%s"' % (self.host, cmd))
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            #print("  |++++++++++command out info begin++++++++++|\n")
            for errline in stderr:
                print('    ', errline.strip())
            for outline in stdout:
                #print('    ', outline.strip())
                out = outline

            #print("\n  |++++++++++ command out info end ++++++++++|")

            return out
        except Exception as e:
            print("execute command %s error, error message is %s" % (cmd, e))

        # print("%s\tFinished!\n" % self.host)

        # 关闭连接
        # self.ssh.close()

    def out_

    def send_cmd(self):
        """交互式命令操作"""
        chan = self.ssh.invoke_shell()
        chan.send('screen -S ')

        for c in cmd:
            chan.send(c)
            out = chan.recv(1024)
            for o in out:
                print(o.strip())

    def upload_file(self, local_file, server_file):
        """上传文件到服务器"""
        t = paramiko.Transport((self.host, self.port))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)

        try:
            print("\nNow Upload Files to %s!" % self.host)
            sftp.put(
                local_file,
                server_file
            )
            print("File Upload Success!!!\n")
        except Exception as e:
            print("Uploads files faild!!!\n%s\n" % e)
            # 上传失败退出程序
            exit()

        t.close()


    def __del__(self):
        """程序退出时关闭连接"""

        self.ssh.close()