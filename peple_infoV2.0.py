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

更新时间：2018/1/9
    优化代码
更新时间：2018/1/10
    所有操作保存到文件
    open    eval   strip   write   codecs
'''
import sys, codecs

errorInfo = '''
+--------------------------------+
|             FAILD              |
 --------------------------------
|                                |
\t%s
+--------------------------------+'''
#userInfoList = []    #保存所有用户信息
#userDeletedList = []   #保存删除用户信息
dyadicList = ['user_info', 'user_deleted']  #二维列表文件

def openFiles(filepath,permission='a+', cod= 'utf-8'):   #读取文件信息到列表
    f = codecs.open(filepath,permission,cod)    
    f.seek(0,)
    infoList = f.readlines()
    for x in range(len(infoList)):
        if filepath in dyadicList:
                #二维列表需要去掉换行符并用eval转换成List
            infoList[x] = eval(infoList[x].strip('\n'))
        else:
            infoList[x] = infoList[x].strip('\n')  #一维列表直接去掉末尾的换行符即可
    return f, infoList
##加载文件信息开始
fileUserInfo, userInfoList = openFiles('user_info')
fileUserDeleted, userDeletedList = openFiles('user_deleted')

def writeFiles(source,filepath,permission='w', cod = 'utf-8'):
    f = codecs.open(filepath,permission,cod)
    for x in source:
        f.write(str(x)+'\n')

def userExists(name):
    someone = 0
    for x in userInfoList:
        if name == x[0]:
            someone = 1
    for x in userDeletedList:
        if name == x[0]:
            someone = 2
    return someone
        

def userInfoShowAll():
    if len(userInfoList) > 0:
        print('''
+-------------------------------------------------------------------------+
|                            所有用户信息                                 |
 -------------------------------------------------------------------------
|                                                                         |''')
        for x in userInfoList:
            print('\n\n姓名：%s  性别：%s  年龄：%s  城市：%s' % (x[0], x[1], x[2], x[3]))
        print('+-------------------------------------------------------------------------+\n')
    else:
        print(errorInfo % ('当前没有任何用户'))

def userNameShowAll():
    if len(userInfoList) > 0:
        print('\n\n所有用户名单：')
        for x in userInfoList:
            print('【    %s    】' %(x[0]), end = '')
    else:
        print(errorInfo % ('当前没有任何用户'))
        return False
        
def userInfoShowOne(*name):
    someone = False
    if len(userInfoList) > 0:
        userNameShowAll()
        if not name:
            name = input('\n请输入要查看的姓名：').strip()
        else:
            name = ''.join(name)
        for x in userInfoList:
            if x[0]== name:
                #print('位置：user[%d]' % (x))
                print('\n\n姓名：%s  性别：%s  年龄：%s  城市：%s' % (x[0], x[1], x[2], x[3]))
                someone = True
        if not(someone):
            print(errorInfo %('查无此人'))
    else:
        print(errorInfo % ('当前没有任何用户'))

        
def userAdd():    #添加用户，姓名不可重复
    user = []  #临时用户表，用来存储单个用户有信息
    bye = False   #退出外层循环判断使用    
    for x in ['姓名', '性别', '年龄', '城市']:
        while 1:   #死循环禁止输入空字符
            d = input('请输入用户 %s: ' % (x)).strip()  # .strip用于去掉前后的空格
            if d != '':
                if x == '姓名' :
                    if userExists(d) != 0:
                        print(errorInfo % ('%s 已经存在' % (d)), end = '')
                        bye = True
                        break   #用户重名退出
                if x == '年龄':
                    while 1 :    #死循环检测年龄输入项是否正确
                        try:
                            d = int(d)
                            break
                        except ValueError as e:
                            print(errorInfo % ('请输入正确的年龄'))
                            d = input('请输入用户 年龄: ').strip()
                break
            else:
                print(errorInfo % ('%s不能为空' % (x)))
        if bye:
            break
        else:
            user.append(d)
    if not bye:
        userInfoList.append(user)
        
        
def userChange():    #修改用户信息
    #userChangeDict = {'1':pass, '2':pass, '3':pass, '4':pass}
    userNameShowAll()
    nameIndex = -1
    e = input('\n要修改的用户姓名：').strip()
    for x in userInfoList:
        if x[0] == e:
            nameIndex = userInfoList.index(x)
    if nameIndex > -1:
        userInfoShowOne(e)
        while 1:    #死循环防止输入选择项有误
            f = input('''
                1：姓名
                2：性别
                3：年龄
                4：城市
            请选择要修改的项目：''').strip()
            if  f in ['1', '2', '3', '4']:
                if int(f) == 1:
                    print('修改前的姓名：%s' %(e))
                    userInput = input('修改后的姓名：').strip()
                    if userExists(userInput) != 0:
                        print(errorInfo %('姓名已存在，修改失败。'))
                        break
                    else:
                        userInfoList[nameIndex][0] = userInput
                elif int(f) == 2:
                    userInfoList[nameIndex][1] = input('请输入修改后的性别：').strip()
                elif int(f) == 3:
                    while 1 :    #死循环防止输入项有误
                        ageNew = input('请输入修改后的年龄：').strip()
                        try:
                            ageNew = int(ageNew)
                            break
                        except ValueError as e:
                            print(errorInfo % ('请输入正确的年龄') )
                    userInfoList[nameIndex][2] = ageNew
                elif int(f) == 4:
                    userInfoList[nameIndex][3] = input('请输入修改后的城市：').strip()
                break    #修改后退出循环
            else:
                print(errorInfo % ('输入有误，请重新输入'))
    else:
        print(errorInfo % ('查无此人：%s' % (e)))

        
def userDelete():   #删除用户
    someone = False
    if userNameShowAll() != False:
        g = input('\n请输入要删除的用户姓名：').strip()
        for x in userInfoList:
            if g in x:
                infoNum = userInfoList.index(x)
                userDeletedList.append(x)
                userInfoList.pop(infoNum)
                print('%s 删除成功！' % (g))
                someone = True
        if not someone:
            print(errorInfo % ('没有此用户'))

def ageThanNum():
    try:
        num = int(input('\n大于等于指定的年龄：'))
        someone = 'no'
        for x in userInfoList:
            if x[2] >= num:
                print(x[0], end = '\t')
                someone = 'yes'
        if someone == 'no':
            print(errorInfo %('没有符合条件的用户'))
    except ValueError as e:  #没有正确输入数字报错
        print(errorInfo % ('请输入正确的数字'))
        
def ageLessNum():
    try:
        num = int(input('\n小于指定的年龄：'))
        someone = 'no'
        for x in userInfoList:
            if x[2] < num:
                print(x[0], end = '\t')
                someone = 'yes'
        if someone == 'no':
            print(errorInfo % ('没有符合条件的用户'))
    except ValueError as e:  #没有正确输入数字报错
        print(errorInfo % ('请输入正确的年龄'))
       
def userDeletedShow():
    if len(userDeletedList) > 0:
        print('已删除用户：')
        for x in userDeletedList:
            print('姓名：%s  性别：%s  年龄：%s  城市：%s' % (x[0], x[1], x[2], x[3]))
    else:
        print(errorInfo % ('当前没有已删除用户'))
        
def exitSystem():
    fileUserInfo.close()
    fileUserDeleted.close()
    writeFiles(userInfoList, 'user_info')
    writeFiles(userDeletedList, 'user_deleted')
    print('退出系统，ByeBye!!')
    sys.exit()

def menuHome():
    menuHomeDict = {'0':exitSystem, '1':menuQuery, '2':menuChange}
    while 1:
        userInput = input('''
            +------------------------------+
            |       用户信息管理系统       |
             ------------------------------
            | 1：用户信息查询              |
            | 2：用户信息增改删            |
            | 0：退出系统并保存            |
            +------------------------------+
        请选择功能：''').strip()
        if userInput and userInput in ['0', '1', '2']:
            menuHomeDict[userInput]()
        else:
            print(errorInfo % ('输入有误，请重新输入'))
    
def menuQuery():
    menuQueryDict = {'0':menuHome, '1':userNameShowAll, '2':userInfoShowOne, '3':ageThanNum, '4':ageLessNum, '5':userDeletedShow}
    while 1:
        userInput = input('''
        +------------------------------+
        |           用户查询           |
         ------------------------------
        | 1：显示所有用户              |
        | 2：用户详细信息              |
        | 3：大于等于指定年龄          |
        | 4：小于指定年龄              |
        | 5：已删除用户                |
        | 0：返回主菜单                |
        +------------------------------+
    请选择功能：''').strip()
        if userInput and userInput in ['0', '1', '2', '3', '4', '5']:
            menuQueryDict[userInput]()
        else:
            print(errorInfo % ('输入有误，请重新输入'))
            
def menuChange():
    menuChangeDict = {'0':menuHome, '1':userAdd, '2':userChange, '3':userDelete}
    while 1:
        userInput = input('''
        +------------------------------+
        |           用户修改           |
         ------------------------------
        | 1：添加用户                  |
        | 2：用户信息修改              |
        | 3：删除用户                  |
        | 0：返回主菜单                |
        +------------------------------+
    请选择功能：''').strip()
        if userInput and userInput in ['0', '1', '2', '3']:
            menuChangeDict[userInput]()
        else:
            print(errorInfo % ('输入有误，请重新输入'))

           
menuHome()  #调用主目录开始