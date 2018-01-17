# -*- coding: utf-8 -*-

# 输入姓名查询成绩

# 录入姓名和成绩
import time

d = {
    '小明': 99,
    '小刚': 83,
    '小芳': 100,
    '小王': 85,
    '小李': 74,
    '小张': 42,
    '小飞': 19
}

# 显示所有录入姓名
print('本次参加考试的人员有：\n')
for k in d:
    print(k, end=" ")

# 用户输入姓名
name = input('\n\n请输入查询姓名：\t')

if name in d:
    print('\n\n', name, '的成绩是：', d[name])
else:
    print('\n\n查无此人')


print(time.strftime('%Y-%m-%d %H:%M:%S'), '星期', time.strftime('%w'))
