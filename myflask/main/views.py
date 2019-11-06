#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
# 数据库模型
from .models import M_SMS
# 短信发送
from .sms_notice import SMS
import time
from flask import jsonify, request, abort, render_template, flash, redirect, url_for, session, current_app
from flask_login import current_user, login_required
import logging

logger = logging.getLogger(__name__)


def all_data():
    """查询所有数据"""
    logger.info('%s', request.url)
    data = M_SMS.query.all()
    # return render_template("all_data.html", data=data)
    # 所有数据以json格式返回
    datas = []
    for d in data:
        if d.status == 0:
            d.status = "失败"
        else:
            d.status = "成功"
        datas.append({
            'id': d.id,
            'ip_addr': d.ip_addr,
            'sms_info': d.sms_info,
            're_mobile': d.re_mobile,
            "status": d.status,
            # 格式化输出时间
            'send_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(d.send_time)),
            'fail_info': d.fail_info
        })
    # return jsonify(data=datas)
    return render_template("show_all.html", data=datas)


def add_data(ip_addr, sms_info, re_mobile, status, fail_info=''):
    """添加一条数据"""
    # 测试数据
    # ip_addr = '2.2.4.8'
    # sms_info = "2019年9月30号测试了一条222"
    # re_mobile = "19994411399"
    # status = '0'
    # send_time = int(time.time())  # 系统当前时间戳
    sms = M_SMS(
        ip_addr=ip_addr,
        sms_info=sms_info,
        re_mobile=re_mobile,
        status=status,
        send_time=int(time.time()),  # 系统当前时间戳
        fail_info=fail_info
    )
    from app import db
    try:
        db.session.add(sms)
        db.session.commit()
    except Exception as e:
        current_app.logger.error('%s', e)
        db.session.rollback()
        db.session.flush()
        result = {'msg': '添加失败'}
        return jsonify(data=result)

    # data = M_SMS.query.filter_by(id=id).first()  # 返回结果中的第一个
    # ########## 添加成功后返回添加的数据
    # result = {
    #     'id' : sms.id,
    #     'ip_addr' : sms.ip_addr,
    #     'sms_info' : sms.sms_info,
    #     're_mobile' : sms.re_mobile,
    #     'status' : sms.status,
    #     'send_time' : sms.send_time
    # }
    # return jsonify(data=result)
    return jsonify(data={'msg': "成功添加到数据库"})


def send_sms():
    """ 发送短信通知 """
    if not request.json:
        abort(400)
    # print("type: ", type(request.json))
    # print(request.json)
    sms = SMS()
    # 接收参数
    result = request.json
    # 手机号
    sms.mobile = result['mobile'] or '19994411399'
    # 发送模板变量内容
    sms.content = result['content']
    # 发送警告
    send = sms.send()
    # 写入库
    content_list = result['content'].split("$$")  # 信息主要内容格式化为 list
    sms_info = "服务器{0[0]}（{0[1]}）的{0[2]}在{0[3]}发生错误：{0[4]}".format(
        content_list)
    if send['code'] == '0':  # 短信接口返回的状态码，0是成功，非0是失败
        add_data(
            ip_addr=content_list[0], sms_info=sms_info, re_mobile=sms.mobile, status=1)
    else:
        add_data(ip_addr=content_list[0], sms_info=sms_info,
                 re_mobile=sms.mobile, status=0, fail_info=send["msg"])
    # return json.dumps(request.json)
    # 返回发送结果
    return send


def hello(username="kk"):
    return "Hello %s !!" % username


def test1():
    return "test1"


def server_info(data='123'):
    return render_template("server_info.html", data=data)

def server_add():
    if request.method == 'POST':
        print("=======>>>", request.form, "长度： ", request.from_values())
        if request.form:
            # flash('Record was successfully added')
            return render_template('server_add.html', data=request.form)

    return render_template('server_add.html')
    # return render_template("info_add.html")

# 后台主页
@login_required
def back_home():
    return render_template("home.html")

def index():
    return render_template("index.html")

def before_app_request():
    print(">>>", request.url)


def after_app_requst(response):
    print("<<<<", response.status)
    return response  # 必须返回一个值，否则会报错
