#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
定制于监控业务出错时发送短信通知使用
"""
# 短信平台 ： 创瑞云
# 模板内容：服务器 {1}@{2} 的 {3} 出现错误：{4}，请及时处理
# 发送的短信内容是模板变量内容，多个变量中间用##或者$$隔开，采用utf8编码

from urllib import request
from urllib import parse

# 接口url
url = "http://api.1cloudsp.com/api/v2/single_send"
accesskey = "k5jL3ujNNMC2rNka"
secret = "6SAlaiRiZRE102ySuZp4zzJdPbWI0UF3"




