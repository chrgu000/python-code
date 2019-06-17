#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# Author: Bing

#
#                         _ooOoo_
#                        o8888888o
#                        88" . "88
#                        (| -_- |)
#                        O\  =  /O
#                     ____/`---'\____
#                   .'  \\|     |    `.
#                  /  \\|||  :  |||    \
#                 /  _||||| -:- |||||-  \
#                 |   | \\\  -  / |     |
#                 | \_|  ''\---/'' |    |
#                 \  .-\__  `-` ___/-. /
#               ___`. .'  /--.--\  `. . __
#            ."" '<  `.___\_<|>_/___.'  >'"".
#           | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#           \  \ `-.   \_ __\ /__ _/   .-` /  /
#      ======`-.____`-.___\_____/___.-`____.-'======
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#    佛祖保佑       永无BUG        轻松上架       6666
#*************************************************************

"""
hosts = []
# 读取配置
with open('config.ini','r') as f:
    for line in f:
        if line[0] != '#':
            hosts.append(line.strip())

# 输出配置文件信息
for i in range(2):
    host = hosts[i].split(',')
    print("IP: {0[0]}  端口号：{0[1]}  用户名：{0[2]}  密码：{0[3]}".format(host))

print(hosts)"""


import urllib
import urllib.request

resp = urllib.request.urlopen('http://www.weather.com.cn/live/?c=114.072154,22.650002').read()



print(type(resp), "\n ===================== \n", resp.decode('utf-8'))

#result = re.findall(r'<span class="temn">(.*)</span>', resp)
#for x in result:
    #print(x)
#result1 = re.findall(r'<div class="txt">(.*)</div>', resp)
#print(result[0], '℃' ,result1[0])


