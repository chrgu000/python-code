#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
使用twilio发送短信通知
"""

from twilio.rest import Client
from time import sleep
import urllib3

# 取消所有urllib3的警告
urllib3.disable_warnings()



# Your Account SID from twilio.com/console
account_sid = "AC4d93f3678ae9e9e47cff0d390127e10c"
# Your Auth Token from twilio.com/console
auth_token  = "601e29ed7a05bf0c548a271f2f0e8aec"

client = Client(account_sid, auth_token)

for i in range(10):
    message = client.messages.create(
        to="+8617006937110", 
        from_="+12063126428",
        body="JUST TEST %s 。" % (str(i)*i))
    sleep(1)

    print(message.sid)