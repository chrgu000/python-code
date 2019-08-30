#!/usr/bin/env python3
#-*- coding:utf-8 -*-


import json
import requests

info = '''
    {
      "enable" : true,
      "password" : "nHHpgf",
      "method" : "aes-256-cfb",
      "remarks" : "ID:%s",
      "server" : "%s",
      "obfs" : "plain",
      "protocol" : "origin",
      "group" : "小白加速器www.xbjsq.me",
      "server_port" : 443,
    },'''

# 读取json数据
with open('server.json.txt', 'r') as f:
    result = json.load(f)["serverlist"]

# 打印读取的结果
#print(type(result), len(result))


# IP地区重复计数
ip_country = {}

for i in result:
    """输出最终结果"""
    # 查询IP所在国家，get请求原始数据
    ip_info = requests.get(url='http://ip.tianqiapi.com/?ip=%s' % i["node_ip"])
    # 读取查询到的数据并格式化
    ip_info = json.loads(ip_info.text)
    print(ip_info)
    #print(info.lstrip('\n') % (i["id"], i["node_ip"]))
    #break

