#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
定制于监控业务出错时发送短信通知使用
"""
# 短信平台 ： 创瑞云
# 模板内容：服务器 {1}@{2} 的 {3} 出现错误：{4}，请及时处理
# 发送的短信内容是模板变量内容，多个变量中间用##或者$$隔开，采用utf8编码

import requests

class SMS():
    """创瑞云发送短信接口"""
    def __init__(self):
        # 接口url
        self.url = "http://api.1cloudsp.com/api/v2/single_send"

        self.data = {
            "accesskey" : "k5jL3ujNNMC2rNka",
            "secret": "6SAlaiRiZRE102ySuZp4zzJdPbWI0UF3",
            # 短信签名或者签名ID
            "sign" : "135539",
            # 短信模板Id
            "templateId" : "159128",
            # 手机号码(只支持单个手机号)
            "mobile" : "19994411399",
            # 模板变量内容，多个变量中间用##或者$$隔开
            "content" : "13.231.45.60$$Geth-test02$$erc20API$$2019-09-23 10:55:12$$出错重启了一次"
        }
    def send(self):
        result = requests.get(self.url, params=self.data)
        return result.json()

if __name__ == '__main__':
    s = SMS()
    print(s.send())

