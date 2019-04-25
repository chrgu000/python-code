#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Author: Bing
# Date: 2018/12/17 15:30

"""
阿里云服务器初始化：
	挂载硬盘
	修改ssh端口为7221
"""
import threading
from server import Server


hosts=[
		'103.112.211.147',
		'103.112.211.69',
		'103.112.211.20',
	]

def server_init(host):
	host=host
	port = 22
	password = '6c7dYzEB5'
	# vmware
	#password = 'wodemima'

	my_server = Server(password=password, port=port, host=host)

	my_server.upload_file(r'script/auto_format_disk.sh', 'auto_format_disk.sh')

	my_server.exec_cmd('chmod +x auto_format_disk.sh')
	my_server.exec_cmd('./auto_format_disk.sh')

	# 安装软件包
	#my_server.exec_cmd('netstat -ntlp' )


for host in hosts:
	thread = threading.Thread(target=server_init, args=(host,))
	thread.start()
