#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#计算任意两个整数间的和并统计偶数和奇数
print('==========任意两个整数间的和================')
num1 = int(input('\n请输入第一个整数：'))
num2 = int(input('\n请输入第二个整数：'))
if num1 > num2:  #如果num1大于num2，则交换值，保证num2大于num1
    num1, num2 = num2, num1
nums = (num1, num2) #声明一个tuple用来存放开始数字和结束数字

#为了统一输出奇数和偶数，用list存储后打印，否则直接print即可！
evens = []  #存储所有偶数
odds = []  #存储所有奇数

numSum = 0
for x in range(num1, num2+1):
    numSum = numSum + x 
    if x % 2 == 0:
        evens.append(x) #在偶数list结尾插入值
        #此处可直接用 print('偶数', x) 来打印出偶数
    else:
        odds.append(x)  #在奇数list结尾插入值
        #此处可直接用 print('奇数', x) 来打印出偶数

print('\n\n从 %d 到 %d 的和为：【 %s 】' %(nums[0],nums[1], numSum), '（注：此结果由for循环完成）')

###统一打印奇数、偶数开始
if len(evens) > 0:
    print( '\n偶数有：')
    for x in evens:
        print('%5d' %(int(x)), end=" ")
else:
    print('\n\n没有偶数')
    
 
if len(odds) > 0:
    print('\n\n奇数有：')
    for x in odds:
        print('%5d' %(int(x)), end=" ")
else:
    print('\n\n没有奇数')
###偶数、奇数打印完毕 
numSum = 0

while num1 <= num2:
    numSum = numSum + num1
    num1 = num1 + 1
    
print('\n\n从 %d 到 %d 的和为：【 %s 】' %(nums[0],nums[1], numSum), '（注：此结果由while循环完成）')

numSum = 0
for x in range(num2+1):
    if (x % 3 == 0) or (x % 5 == 0):  #计算3、5倍数和
        numSum = numSum + x
        
print('\n\n%d—%d间3、5倍数和：【 %d 】' % (nums[0], nums[1], numSum))