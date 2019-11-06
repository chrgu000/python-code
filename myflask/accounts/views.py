#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import url_for, redirect, request, render_template, flash
from flask_login import login_user, logout_user, login_required
from app import login_manager
from .models import User

# 用户记录表
users = [
    {'username': 'Tom', 'password': '111111'},
    {'username': 'Bob', 'password': '123456'},
]

#### 用户验证
# 实验，用一个 dict 记录用户
# 通过用户名查询用户记录，如果不存在，返回None
def query_user(username):
    for user in users:
        if user['username'] == username:
            return user

# 如果用户存在，构建一个新的用户类对象，并使用用户名作为ID
# 如果不存在，必须返回None
@login_manager.user_loader
def load_user(username):
    if query_user(username) is not None:
        curr_user = User()
        curr_user.id = username
        return curr_user

# 从请求参数中获取用户名
@login_manager.request_loader
def load_user_from_request(requtest):
    username = request.args.get('username')
    if query_user(username) is not None:
        curr_user = User()
        curr_user.id = username
        return curr_user

# 用户登录
def login():
    print("next: ", request.args.get('next'))
    if request.method == 'POST':
        username = request.form.get('username')
        user = query_user(username)
        # 验证用户名及密码
        if user is not None and user['password'] == request.form['password']:
            curr_user = User()
            curr_user.id = username

            # 通过 Flask-Login的login_user方法登录用户
            login_user(curr_user)

            # 如果请求中有next返回上一页，没有就返回index
            next = request.args.get('next')
            return redirect(next or url_for("main.back_home"))

        flash("Wrong username or password")
    # GET请求
    return render_template("accounts/login.html")

# 注销用户
@login_required
def logout():
    # 调用系统方法注销用户
    logout_user()
    return redirect("/")

# 用户注册
def register():
    return render_template("accounts/register.html")
