# -*- coding: utf-8 -*-
'''
用户随意输入一个字符串，是否含有'f','r','i','e','n','d'六个字符，
有则拼接成'friend'，输出到屏幕并统计组成了几个
'''

word = input('请输入任意字符（多位）：')

wordF = ['f', 'r', 'i', 'e', 'n', 'd']
wordN = {}
wordX = []
for x in wordF:
    wordN[x] = word.count(x)
    wordX.append(wordN[x])
    if x in word:
        print('输入的字符中包含%d个%s' % (word.count(x), x))
    else:
        print('输入的字符中不包含%s' % (x))
print(wordN)
friendX = '可以组成%d个"friend"'
n = 0
while n <= max(wordX):
    if n in wordX:
        print(friendX % (n), end)
        break
    n += 1