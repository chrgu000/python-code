#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
使用HTMLParser解析
https://www.python.org/events/python-events/
输出会议时间、名称、地点
"""

from urllib import request
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.on_off = False #  匹配数据总开关
        self.info = False # 提取所需信息开关
        self.dd = {'events':[], 'missed':[]}
        self.key_word = 'events' # 存放数据key值
        self.n = 0 # 计数，让两部分日期合并

    def handle_starttag(self, tag, attrs):
        if tag == 'ul' and ('class','list-recent-events menu') in attrs:
            #print('1')
            self.on_off = True

        if tag == 'aside' and ('class', 'right-sidebar') in attrs:
            self.on_off = False

        if tag in ('time', 'a', 'span') and self.on_off:
            #print('2')
            self.info = True
        else:

            self.info = False

    def handle_endtag(self, tag):
        self.info = False


    def handle_data(self, data):

        if data == 'You just missed...':
            self.key_word = 'missed'

        if self.info:
            self.n += 1
            if self.n == 3:
                self.dd[self.key_word][-1] += '(%s)' % data.strip()
                self.dd[self.key_word][-1] = self.dd[self.key_word][-1].replace('.', '')
            else:
                self.dd[self.key_word].append(data)
            if self.n == 4:
                self.n = 0

    def __str__(self):
        '''格式化打印输出'''
        p_str = ''
        m = 0
        for key in self.dd.keys():
            if key == 'events':
                p_str += 'Upcoming Events\n\n'
            elif key == 'missed':
                p_str += '\n\nYou just missed...\n\n'
            for x in range(int(len(self.dd[key])/3)):
                p_str += '  Title: {}\n  Date: {}\n  Place: {}\n\n'.format(*self.dd[key][m*3:m*3+3])
        return p_str

# 测试
with request.urlopen('https://www.python.org/events/python-events/') as f:
    url_data = f.read().decode('utf-8')

parser = MyHTMLParser()
parser.feed(url_data)
#print(parser.dd)
print(parser)