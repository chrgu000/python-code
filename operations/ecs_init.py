#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Author: Bing
# Date: 2018/12/17 15:30

"""
阿里云服务器初始化：
	挂载硬盘
	修改ssh端口为7013
"""
import threading
from server import Server
#import ss5


hosts=[


	'47.52.233.73',

	]

def server_init(host):
	host=host
	port = 7013
	password = r'qarwdJpfiF31'
	#password = 'wodemima'  # vmware
	script_file = r'auto_format_disk.sh'
	script_file = r'install_jdk.sh'


	my_server = Server(password=password, port=port, host=host)

	#my_server.upload_file("./script/%s" % script_file, script_file)
	#my_server.exec_cmd('chmod +x %s' % script_file)
	#my_server.exec_cmd('sh %s' % script_file)

    # windows 上传脚本文件格式需要转换，直接从github上下载执行
    # 完成后删除脚本文件
	my_server.exec_cmd('''curl -LJO https://raw.githubusercontent.com/WWBING/python-code/master/mochain/script/{sf} \
    && sh {sf} \
    && rm -rf {sf}'''.format(sf = script_file))

	# 安装软件包
	#my_server.exec_cmd('netstat -ntlp' )


for host in hosts:
	thread = threading.Thread(target=server_init, args=(host,))
	thread.start()
