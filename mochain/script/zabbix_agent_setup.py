# /usr/bin/env python3
# -*- coding: utf-8 -*-
# author:
"""
设置服务器加入zabbix
"""
from server import Server
import threading

def setup():
    pass

hosts = (
    ("192.168.50.5", 22, 'wodemima'),
    ('192.168.50.6', 22, 'wodemima'),
    ('192.168.50.7', 22, 'wodemima')
    )

step = [
    "yum -y install zabbix-agent zabbix-sender",
    'sed -i "s/Server=127.0.0.1/Server=192.168.50.88/" /etc/zabbix/zabbix_agentd.conf',
    "sed -i 's/ServerActive=127.0.0.1/ServerActive=192.168.50.88/' /etc/zabbix/zabbix_agentd.conf",
    "sed -i 's/Hostname=Zabbix server/#Hostname=Zabbix server/' /etc/zabbix/zabbix_agentd.conf",
    "sed -i '170iHostMetadata=Linux 9TuT9PyOCPZqUpQ6AWoQ9V2kS3exYt' /etc/zabbix/zabbix_agentd.conf",
    "systemctl enable zabbix-agent",
    "systemctl restart zabbix-agent"
]

def zabbix_agent_install(host, port, password):
    my_server = Server(host, port, password)
    out = my_server.exec_cmd("rpm -qa | grep zabbix-agent")
    if not out:
        my_server.upload_file(
                r"F:\迅雷下载\zabbix-release-4.0-1.el7.noarch.rpm",
                r"/root/zabbix-release-4.0-1.el7.noarch.rpm"
            )
        my_server.exec_cmd("rpm -ivh zabbix-release-4.0-1.el7.noarch.rpm")
        for m in step:
            my_server.exec_cmd(m)
        print("success!")
    else:
        print("\n【 %s 】已安装！\n" % host)


for host in hosts:
    my_thread = threading.Thread(
        target=zabbix_agent_install,
        args=(host[0], host[1], host[2])
        )
    my_thread.start()
    my_thread.join()