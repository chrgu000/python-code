#-*- coding: utf-8 -*-
'''
小游戏，课程学习用
创建日期：2017/12/29
更新日期：2018/1/8
    添加九宫格地图
    九宫格内移动
'''

import time, sys

print("welcome to Hero's world!!")

user_id = input("请输入用户名：")
user_pwd = input('请输入密码：')
# time.sleep(2)  #等待2秒
print('\n账号注册中 ')
###注册进度，模拟真实，闹着玩儿！！2333333
for x in range(1, 11):
    time.sleep(0.4)
    print('.'*x, x * 10, '%', end = '')

print('''
恭喜，账号注册成功！！！
\t+------------------+
\t|    请妥善保管    |
\t|------------------|
\t|账号：%-12s|
\t|密码：%-12s|
\t+------------------+
''' % (user_id, user_pwd))

if input('按下回车键进入游戏，其它任意键退出游戏：') == '':
    for x in range(1, 11):

        print('Loading%s%d%%' % ('.'*x, x*10))
        time.sleep(2)

    print('加载游戏成功！！')
else:
    print('游戏将在5秒后退出')
    time.sleep(2)
    sys.exit()


user_name = input('\n请输入角色昵称：')
user_gender = input('请选择性别（0为男性，1为女性）：')

if user_name == '':
    user_name = '开局一把刀'
if user_gender == '' or user_gender == '0':
    user_gender = '男'
elif user_gender == '1':
    user_gender = '女'
    
print('''
+--------------------------+
| 昵称：%s
| 性别：%s
+--------------------------+''' % (user_name, user_gender))
time.sleep(10)   #暂停5秒查看信息
map = ((0, 2), (1, 2), (2, 2),
(0, 1), (1, 1), (2, 1),
(0,0), (1, 0), (2, 0))
mapZh = ('''世界地图：九宫格
+-----------------+
|(0,2)|(1,2)|(2,2)|
 -----------------
|(0,1)|(1,1)|(2,1)|
 -----------------
|(0,0)|(1,0)|(2,0)|
+-----------------+
初始位置： %s ''')
xyz = 6   #默认坐标map[6]
while 1 :
    print('\n\n%s\n当前位置： %s ' %(mapZh % (map[6],), map[xyz]))
    userInp = input('''    +-----------+
    |按'a'键向左|
    |按'd'键向右|
    |按'w'键向上|
    |按's'键向下|
    +--------------+
    |'quit'退出游戏|
    +--------------+
请选择移动方向：''')
    if userInp in ['w', 's', 'a', 'd']:
        if userInp == 'w':
            if xyz - 3 >= 0:
                xyz -= 3
        if userInp == 's':
            if xyz + 3 <= 8:
                xyz += 3
        if userInp == 'a':
            if xyz - 1 >= 0 and xyz not in [3, 6]:  #左边缘时不移动
                xyz -= 1
        if userInp == 'd':
            if xyz + 1 <= 8 and xyz not in [2, 5, 8]:  #右边缘时不移动
                xyz += 1
    elif  userInp == 'quit':
        print('\n\nBye!!!')
        break
    else:
        print('\n\n请选择正确的方向！！\n')