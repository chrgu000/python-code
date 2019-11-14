#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试 flask-login模块
"""

from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user

app = Flask(__name__)
login_manager = LoginManager(app)

app.secret_key = '123456'
login_manager.login_view = 'login'
login_manager.login_message = ''
login_manager.login_message_category = 'info'
login_manager.session_protection = "strong"
login_manager.init_app(app)


class User(UserMixin):
    pass


# 用户记录表
users = [
    {'username': 'Tom', 'password': '111111'},
    {'username': 'Bob', 'password': '123456'},
]

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


@app.route('/login', methods=['GET', 'POST'])
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
            return redirect(next or url_for("home"))

        flash("Wrong username or password")
    # GET请求
    return render_template("login.html")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/back/home')
@login_required
def home():
    return render_template("home.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        print("=======>>>", request.form, "长度： ", request.from_values())
    return render_template("info_add.html")


if __name__ == '__main__':
    app.run(debug=True)
