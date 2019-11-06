#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
路由
"""

from flask import Blueprint, g

from . import views

main = Blueprint('main', __name__)

main.add_url_rule("/", "index", views.index)
main.add_url_rule("/all",  view_func=views.all_data)
main.add_url_rule('/hello/<username>', "hello", view_func=views.hello, methods=['POST', 'GET'])
main.add_url_rule('/hello', view_func=views.hello, methods=['POST', 'GET'])
main.add_url_rule('/test1', "test1", views.test1)
# main.add_url_rule('/login', view_func=views.login, methods=['GET', "POST"])
############ cur post 请求格式
# 传 json  {'mobile': ""， "content" : "**$$**$$***$$***$$***"}
# curl -i -H "Content-Type: application/json" -X POST -d '{"mobile" : "19994411399", "content" : "13.231.45.60$$Geth-test02$$erc20API$$2019-10-15 12:55:12$$出错重启了一次"}' http://localhost:5000/monitor/sms
main.add_url_rule('/monitor/sms', "sms", views.send_sms, methods=['POST'])

main.add_url_rule('/back/server_info', view_func=views.server_info)
main.add_url_rule('/back/home', view_func=views.back_home)
main.add_url_rule('/back/server_add', view_func=views.server_add, methods=['GET', 'POST'])

# main.before_app_request(views.before_app_request)
# # main.after_app_request(views.after_app_requst)
