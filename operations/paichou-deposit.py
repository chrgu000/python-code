#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
公司派筹项目，通过钱包地址充值金额
"""

import requests
import json 
from lxml import etree

# 测试服配置
url = "https://exchange.gwallet.shop/portal/admin_recharge/add.html"
cookies = dict(PHPSESSID="h9kd2rl95fqd4n9vkrgv1tnn10", admin_username="admin")
# 正式服配置
# url = "https://exchange.gwallet.shop/portal/admin_recharge/add.html"
# cookies = dict(PHPSESSID="d8vkg0o8qnvqiuluk2rmlrs9e0", admin_username="admin")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",

}
# 后台增加资产需要的参数
data = {
    # 钱包地址
    "address":"0ddx1ecbbf7735abe31d9a6251e9ed064ab1b5d9a4dd", 
    # 添加金额
    "recharge_amount" : "2",
    # 操作人
    "responsible" : "tt",
    # 备注 
    "remark" : ""
}

success = []  # 保存成功
err = []  # 保存失败的

# 屏蔽关于https的报错
requests.packages.urllib3.disable_warnings()
with requests.Session() as s:  # 持续会话
    reponse = s.post(url, data=data, headers=header, verify=False, cookies=cookies)

    # print(reponse.text)
    print(reponse.headers)
    exit()
    deposit = reponse.json()
    if deposit['code'] != '1':
        err.append("%s %s" % (data['address'], deposit['msg']))
    else:
        success.append("%s %s" % (data['address'], deposit['msg']))

# 最终输出结果
print('\n\n\t成功的：', success, "\n", "\t失败的：", err)
# 保存结果到文件
with open(r'D:\Users\Personal\Desktop\PaiChou-deposit.txt', 'w') as f:
    f.write("成功的：\n",)
    for s in success:
        f.write(s+"\n")
    f.write("失败的：\n")
    for e in err:
        f.write(e+"\n")