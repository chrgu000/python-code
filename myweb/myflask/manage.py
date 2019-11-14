#!/usr/bin/env python3
#-*- coding: utf-8 -*-


# 本意是做个系统通知短信发送记录
# 慢慢在扩展其它系统



from app import create_app

app = create_app('dev')  # dev是本地开发，区别debug开关

if __name__ == '__main__':
    app.run()
 