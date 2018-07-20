#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
通常我们用一个Socket表示“打开了一个网络链接”
打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型
"""

import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET指定使用IPv4协议，AF_INET6表示IPv6  SOCK_STREAM指定使用TCP协议

# 建立连接：
s.connect(('www.sina.com.cn', 80))

# 发送数据：
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据：
buffer = []
while True:
    # 每次最多接收1K字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

# 关闭连接：
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件：
with open('sina.html', 'wb') as f:
    f.write(html)