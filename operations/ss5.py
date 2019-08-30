#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
使用sockets5代理
"""

import socks
import socket

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'cs.mochain.co', 9888, False, 'mochain', 'mPQ7V2aC')
socket.socket = socks.socksocket