#-*- coding: utf-8 -*-
'''
列表的作业
    可以添加用户及信息（姓名、性别、年龄、城市）
    可以查找用户并显示所有信息
    可以删除用户（存到另一张表里）
    查找年龄小于18岁的人
实际功能：
    显示所有用户 （仅姓名）
    查看用户信息 （指定姓名，显示姓名、性别、年龄、城市）
    查看大于等于指定年龄的用户
    查看小于指定年龄的用户
    添加用户
    修改用户
    删除用户
    查看删除用户
    *注：姓名作为唯一值，不可重复
最后修改时间：2018/1/9
'''
userName = []   #保存所有用户姓名
users = []    #保存所有用户信息
usersDel = []   #保存删除用户信息

def userShowAll():
    if len(users) > 0:
        for x in range(len(users)):
            print('姓名：%s  性别：%s  年龄：%s  城市：%s' % (users[x][0], users[x][1], users[x][2], users[x][3]))
    else:
        print('没有用户')

def userNameShow():
    if len(userName) > 0:
        print('所有用户名单：\n', end = '')
        for x in userName:
            print('%12s' %(x), end = '')
    else:
        print('\n当前没有用户！！')
        
def userAdd():    #添加用户，姓名不可重复
    userInfo = []  #临时用户表，用来存储单个用户有信息
    bye = False   #退出外层循环判断使用    
    for x in ['姓名', '性别', '年龄', '城市']:
        while 1:   #死循环禁止输入空字符
            d = input('请输入用户 %s: ' % (x)).strip()  # .strip用于去掉前后的空格
            if d != '':
                if x == '姓名' :
                    if d in userName:
                        print('\n %s 已经存在！' % (d), end = '')
                        bye = True
                        break   #用户重名退出
                    else:
                        userName.append(d)
                if x == '年龄':
                    while 1 :    #死循环检测年龄输入项是否正确
                        try:
                            d = int(d)
                            break
                        except ValueError as e:
                            print('！！！请输入正确的年龄！！！')
                            d = input('请输入用户 年龄: ').strip()
                break
            else:
                print('%s不能为空！' % (x))
        if bye:
            break
        else:
            userInfo.append(d)
    if len(userInfo) > 0:
        users.append(userInfo)
        return True
        
def userChange():    #修改用户信息
    e = input('\n要修改的用户姓名：').strip()
    if e in userName:
        infoNum = userName.index(e)
        while 1:    #死循环防止输入选择项有误
            f = input('''
            1：姓名
            2：性别
            3：年龄
            4：城市
        请选择要修改的项目：''').strip()
            if f in ['1', '2', '3', '4']:
                if int(f) == 1:
                    print('修改前的姓名：%s' %(e))
                    e1 = input('修改后的姓名：').strip()
                    if e1 in userName:
                        print('姓名重复，修改失败。')
                        break
                    else:
                        userName[infoNum] = e1
                        users[infoNum][0] = userName[infoNum]
                elif int(f) == 2:
                    users[infoNum][1] = input('请输入修改后的性别：').strip()
                elif int(f) == 3:
                    while 1 :    #死循环防止输入项有误
                        ageNew = input('请输入修改后的年龄：').strip()
                        try:
                            ageNew = int(ageNew)
                            break
                        except ValueError as e:
                            print('！！！请输入正确的年龄！！！') 
                    users[infoNum][2] = ageNew
                elif int(f) == 4:
                    users[infoNum][3] = input('请输入修改后的性别：').strip()
                return True
                break    #修改后退出循环
            else:
                print('\n输入有误')
    else:
        print('用户名输入错误！！请确认后再次修改！')
        
def usersDelete():   #删除用户
    userShowAll()
    g = input('请输入要删除的用户姓名：').strip()
    if g in userName:
        infoNum = userName.index(g)
        userName.remove(g)
        usersDel.append(users[infoNum])
        users.pop(infoNum)
        return True


        
while 1:   #死循环
    a = input('''
    +------------------------------+
    |         用户管理系统         |
     ------------------------------
    | 1：显示所有用户              |
    | 2：查看用户信息              |
    | 3：查看大于等于指定年龄的用户|
    | 4：查看小于指定年龄的用户    |
    | 5：添加用户                  |
    | 6：修改用户                  |
    | 7：删除用户                  |
    | 8：查看删除用户              |
    | 0：退出                      |
    +------------------------------+
请选择功能：''').strip()
    if a and a in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
        if a == '0':
            print('\n退出系统，ByeBye!!\n')
            break    #退出程序
        elif a == '1':  #显示所有用户
            userNameShow()
        elif a == '2':   #查看指定用户信息
            userNameShow()
            b = input('\n请输入要查看的姓名：').strip()
            if len(userName) > 0 and b in userName:

                for x  in range(len(users)):
                    if users[x][0]== b:
                        #print('位置：user[%d]' % (x))
                        print('姓名：%s  性别：%s  年龄：%s  城市：%s' % (users[x][0], users[x][1], users[x][2], users[x][3]))
            else:
                print('\n查无此人！！')
        elif a == '3':  #查看大于等于指定年龄的所有用户
            try:
                c = int(input('\n大于等于指定的年龄：'))
                someone = 'no'
                for x in range(len(users)):
                    if users[x][2] >= c:
                        print(users[x][0], end = '\t')
                        someone = 'yes'
                if someone == 'no':
                    print('\n没有符合条件的用户！！')
            except ValueError as e:  #没有正确输入数字报错
                print('\n！！！请输入正确的数字！！！！')
        elif a == '4':   #查看小于指定年龄的用户
            try:
                d = int(input('\n小于指定的年龄：'))
                someone = 'no'
                for x in range(len(users)):
                    if users[x][2] < d:
                        print(users[x][0], end = '\t')
                        someone = 'yes'
                if someone == 'no':
                    print('\n没有符合条件的用户！！')
            except ValueError as e:  #没有正确输入数字报错
                print('\n！！！请输入正确的年龄！！！！')
        elif a == '5':   #添加用户
            if userAdd():
                print('\n用户 “ %s ” 添加成功' % (users[-1][0]))
            else:
                print('添加失败！！')

        elif a == '6':  #修改用户
            userNameShow()
            if userChange():
                print('用户信息修改完毕')
        elif a == '7':   #删除用户
            userNameShow()
            if usersDelete():
                print('删除用户 %s 成功！！！！' % (usersDel[-1][0]))
            else:
                print('\n找不到用户，请核查姓名后重试！！！')
        elif a == '8':   #查看已删除用户
            if len(usersDel) > 0:
                print('已删除用户：')
                for x in range(len(usersDel)):
                    print('姓名：%s  性别：%s  年龄：%s  城市：%s' % (usersDel[x][0], usersDel[x][1], usersDel[x][2], usersDel[x][3]))
            else:
                print('当前没有已删除用户！')

    else:
        print('\n输入有误，请重新输入！！\n')
    
