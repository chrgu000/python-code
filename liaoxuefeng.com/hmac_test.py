#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#Authon: WangBai

"""
hmac的练习
模拟用户注册和登录验证
"""

import hmac
import json
import random


class File_data:
    """数据文件操作"""
    def write_data(self, username, key, hashpassword):
        """保存数据到文件json"""
        if self.read_data():
            load_data = self.read_data()
        else:
            load_data = {}
        print(load_data)
        load_data[username] = (key, hashpassword)

        with open('users_hmac.json', 'w') as f:
            json.dump(load_data, f, ensure_ascii=False)
            print("注册成功：%s" % username)

    def read_data(self):
        """从文件读取数据"""
        try:
            with open('users_hmac.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print('文件不存在。')
        except PermissionError:
            print('权限不足。')
        except:
            pass



class User:
    """用户注册与验证"""
    def __init__(self, username, password):
        """初始化属性"""
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = self.hmac_md5(self.key, password)

    def hmac_md5(self, key, s):
        """生成hmac值"""
        return hmac.new(key.encode('utf-8'),
                        s.encode('utf-8'),
                        digestmod='MD5').hexdigest()

    def regist(self):
        """注册保存到文件"""
        File_data().write_data(
            self.username, self.key, self.password,
            )

    def authentication(self, username, password):
        """登陆认证"""
        if File_data().read_data():
            load_data = File_data().read_data()
            if username in load_data:
                if load_data[username][1] == self.hmac_md5(load_data[username][0], password):
                    print("登陆成功！")
                else:
                    print("密码错误！")
            else:
                print("用户名不存在")
        else:
            print("用户名不存在!")

while True:
    result_uesr = input("1:登陆\t2:注册：")
    if result_uesr == '1':
        result_name = input("请输入用户名：")
        result_pass = input("请输入密码：")
        User(result_name, result_pass).authentication(result_name, result_pass)
    elif  result_uesr == '2':
        result_name = input("请输入用户名：")
        result_pass = input("请输入密码：")
        User(result_name, result_pass).regist()
    else:
        pass
