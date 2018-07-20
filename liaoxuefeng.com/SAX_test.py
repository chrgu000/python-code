#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
SAX处理xml文件读取需要的日期、温度
"""

from xml.parsers.expat import ParserCreate
from urllib import request


class DefaultSaxHandler:
    def __init__(self):
        self.weather = {}
        self.weather['forecasts'] = []

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.weather['city'] = attrs['city']
        if name == 'yweather:forecast':
            self.weather['forecasts'].append({'date':attrs['date'], 'high':attrs['high'], 'low':attrs['low']})

    def __str__(self):
        """打印输出格式化"""
        info_str = ''
        for data in self.weather['forecasts']:
            info_str += '日期：{}  最高温度：{}  最低温度：{}  \n'.format(*data.values())
        return '城市：{} \n{}'.format(self.weather['city'], info_str)

def parseXml(xml_str):
    if not xml_str:
        return
    #print(xml_str)
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml_str)
    print(handler)
    return handler.weather
    return {
        'city': '?',
        'forecast': [
            {
                'date': '2017-11-17',
                'high': 43,
                'low' : 26
            },
            {
                'date': '2017-11-18',
                'high': 41,
                'low' : 20
            },
            {
                'date': '2017-11-19',
                'high': 43,
                'low' : 19
            }
        ]
    }

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'