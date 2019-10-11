#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
短信发送主程序
"""

from app import creat_app


app = creat_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
