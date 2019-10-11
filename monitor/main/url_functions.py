#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""

"""

from .models import M_SMS
from .sms_notice import SMS
import time
from flask import jsonify, request, abort


def all_data():
    """查询所有数据"""
    data = M_SMS.query.all()
    datas = []
    for d in data:
        datas.append({
            'id': d.id,
            'ip_addr' : d.ip_addr,
            'sms_info' : d.sms_info,
            're_mobile' : d.re_mobile,
            "status" : d.status,
            # 格式化输出时间
            'send_time' : time.strftime("%Y%m%d %H:%M:%S", time.localtime(d.send_time))
        })
    return jsonify(data=datas)


def add_data(db):
    """添加一条数据"""
    ip_addr = '2.2.4.8'
    sms_info = "2019年9月30号测试了一条222"
    re_mobile = "19994411399"
    status = '0'
    send_time = int(time.time())
    sms = M_SMS(
        ip_addr = ip_addr,
        sms_info = sms_info,
        re_mobile = re_mobile,
        status = status,
        send_time = send_time
    )
    
    try:
        db.session.add(sms)
        db.session.commit()
    except:
        db.session.rollback()
        db.session.flush()
    id = sms.id
    if (id is None):
        result = {'msg':'添加失败'}
        return jsonify(data=result)

    data = M_SMS.query.filter_by(id=id).first()
    result = {
        'id' : sms.id,
        'ip_addr' : sms.ip_addr,
        'sms_info' : sms.sms_info,
        're_mobile' : sms.re_mobile,
        'status' : sms.status,
        'send_time' : sms.send_time
    }
    return jsonify(data=result)
    

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
    # return json.dumps(request.json)
    # 返回发送结果
    return send

def hello(username="kk"):
    return "Hello %s !!" % username