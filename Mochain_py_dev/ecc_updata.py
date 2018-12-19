#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: xiaobing
# update: 2018/11/19

"""
ecc公链钱包更新
    1.停止两个服务器的ecc服务
    2.删除服务器上的ECC.jar包
    3.上传最新的ECC.jar包
    4.启动两个服务器的ecc服务
"""

from server import Server
import time
import sys


hosts = {
    'ecc': {
        "host" : [ '47.75.211.100', '47.75.244.39'],
        "passwd" : "1Qaz2wsx",
        "port"     : 22,
        # 以下是本地测试
        #"host" : [ '192.168.50.6', '192.168.50.7'],
        #"passwd" : "wodemima",
        #"port" : 22,
        "service" : ["ecc", "register"],
        "servie_port" : [8181, 8899],
        "local_path" : [
            r"C:\Users\WWWBBB\Desktop\工作文档\Ecc钱包\ECC.jar",
            r"C:\Users\WWWBBB\Desktop\工作文档\Ecc钱包\register\register-0.0.1-SNAPSHOT.jar",
        ],
        "remote_path" : [
            r"/data/ecc/ECC.jar",
            r"/data/register/register-0.0.1-SNAPSHOT.jar",
        ]

    },
    'icc': {
        'host' : [ '47.75.167.35', '47.244.131.39'],
        "passwd" : "hNNKvb36f0",
        "port"     : 6221,
        "service" : [ "icc", "register"],
        "servie_port" : [8181, 8899],
        "local_path" : [
            r"C:\Users\WWWBBB\Desktop\工作文档\ICC\ICC.jar",
            r"C:\Users\WWWBBB\Desktop\工作文档\ICC\register\icc-register-0.0.1-SNAPSHOT.jar",
        ],
        "remote_path" : [
            r"/data/icc/ICC.jar",
            r"/data/register/icc-register-0.0.1-SNAPSHOT.jar",
        ],
    }
}


def my_update(host, program):

    my_servers = []
    for i in range(2):
        # 连接到两个 ecc 服务器
        my_server = Server(
                host['host'][i],
                host['port'],
                host['passwd']
            )
        my_servers.append(my_server)
        # 停止两台服务器的 ecc 服务
        my_server.exec_cmd("systemctl stop %s" % host['service'][program])

    # 删除服务器上的 文件
    # 由于在共用磁盘上，所有只需要在一台上执行删除命令
    my_servers[0].exec_cmd("rm -rf %s"  % host['remote_path'][program])
    # 上传新文件到服务器
    # 可以拖动文件到窗口
    file_path = input("input your file full path : ")
    if file_path:
        host['local_path'][program] = file_path
    my_servers[0].upload_file(
        host['local_path'][program],
        host['remote_path'][program]
        )

    # 先分别启动 ecc 服务
    for i in range(2):
        my_servers[i].exec_cmd("systemctl start %s" % host['service'][program])
    print("Wait for the service to start : \n")
    for i in range(55):
        sys.stdout.write(">")
        sys.stdout.flush()
        time.sleep(0.1)  # 休眠, 等待服务启动
    # 查询端口监听状态以判断服务是否启动成功
    for i in range(2):
        my_servers[i].exec_cmd("netstat -ntunlp | grep %s" % host["servie_port"][program])


while True:
    print("""
        请选择项目：
            1： ASTC(ecc)\t\t2： ICC

        """)
    # 输入选择项，错误重新输入
    project = input("输入 1 或者 2：） ")

    if project in ('1', '2'):
        print("""
        请选择项目：
            1： 公链钱包\t\t2： 注册中心

        """)
        # 选择应用程序
        program = input("输入 1 或者 2：） ")
        if program in ('1', '2'):
            program = int(program)-1  # 下标需要减1
            if project == '1':
                my_update(hosts['ecc'], program)
            elif project == '2':
                my_update(hosts['icc'], program)

            break  # 成功执行后退出循环
    print("\n输入有误！重新输入!\n\n")

print("\n\n")
input("ALL DONE !! press enter ty exit.")
