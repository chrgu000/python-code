#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 短信平台 ： 助通

import requests, time
from hashlib import md5

class SMS():
    """创瑞云发送短信接口"""
    def __init__(self):
        # 接口url
        self.url = "http://www.ztsms.cn/sendNSms.do"

        self.data = {
            "username" : "HEJ66",
            # 当前时间
            "tkey": time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())),
            # 密码
            "password" : "dY4VGOwj",
            # 产品ID
            "productid" : "190515",
            # 手机号码(只支持单个手机号)
            "mobile" : "13896810964",
            # 内容
            "content" : "【GIC20】发个短信让你知道助通可以用了，验证码: 666666"
        }
    def send(self):
        result = requests.get(self.url, params=self.data)
        # return result.json()
        return result.text

if __name__ == '__main__':
    s = SMS()
    # s_b = md5(s.data['password'].encode('utf-8')).hexdigest()
    # print(type(s_b))
    s.data['password'] = md5(((md5(s.data['password'].encode('utf-8')).hexdigest()) + s.data['tkey']).encode('utf-8')).hexdigest()
    print(s.send())

