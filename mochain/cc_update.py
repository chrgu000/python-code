#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: xiaobing
# date: 2018/11/19

"""
update: 2018/12/26
    通过配置文件进行更新
update: 2018/11/19
    ecc公链钱包更新
        1.停止两个服务器的ecc服务
        2.删除服务器上的ECC.jar包
        3.上传最新的ECC.jar包
        4.启动两个服务器的ecc服务
"""

from server import Server
import time
import sys
import threading
import codecs


hosts = []
# 读取配置
with codecs.open('config.ini', 'r', 'utf-8') as f:
    for line in f:
        if line[0] != '#':
            hosts.append(line.strip())

if hosts[0] == hosts[1]:
    host_num = 1
else:
    host_num = 2


# 输出配置文件信息
print("\n")
for i in range(host_num):
    host = hosts[i].split(',')
    print("  IP: {0[0]}  端口号：{0[1]}  用户名：{0[2]}  密码：{0[3]}".format(host))

service = hosts[4].split(',') # 服务名和端口号

print("""
    上传本地文件 : {}
    上传后的文件 : {}
    服务的名称   : {}
    服务的端口   : {}
    \n\n""".format(hosts[2], hosts[3], service[0], service[1]))

result = input("输入服务的名称以确认继续（ %s ）：" % service[0])

if result != service[0]:
    sys.exit()


def do_cmd(server, cmd, n=2):
    """n个server同时执行cmd命令"""
    for i in range(n):
        t = threading.Thread(target=server.exec_cmd, args=(cmd,))
        t.start()


# 保存服务器连接，用来两台服务器分别执行命令
my_servers = []
for i in range(host_num):
    host = hosts[i].split(',')
    # 连接到两个 ecc 服务器
    my_server = Server(
            host[0],
            int(host[1]),  # 端口转换成int
            host[3],
            username=host[2]
        )
    my_servers.append(my_server)
    # 停止两台服务器服务
    my_server.exec_cmd("systemctl stop %s" % service[0])

# 删除服务器上的 文件
# 由于在共用磁盘上，所有只需要在一台上执行删除命令
my_servers[0].exec_cmd("rm -rf %s"  % hosts[3])
# 上传新文件到服务器
my_servers[0].upload_file( hosts[2], hosts[3])

# 启动服务
for i in range(host_num):
    my_servers[i].exec_cmd("systemctl start %s" % service[0])
print("Wait for the service to start : \n")
for i in range(55):
    sys.stdout.write(">")
    sys.stdout.flush()
    time.sleep(0.3)  # 休眠, 等待服务启动
# 查询端口监听状态以判断服务是否启动成功
for i in range(host_num):
    my_servers[i].exec_cmd("netstat -ntunlp | grep %s" % service[1])


print("\n\n")
input("ALL DONE !! press enter to exit.\n\n")
