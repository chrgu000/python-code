#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
操作数据库
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from flask import jsonify


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost:3306/monitor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
db.init_app(app)

class M_SMS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_addr = db.Column(db.String(15), nullable=False)
    sms_info = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    send_time = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'host %r' % self.ip_addr

@app.route("/all")
def get_data():
# 查询所有数据
    data = M_SMS.query.all()
    datas = []
    for d in data:
        datas.append({
            'id': d.id,
            'ip_addr' : d.ip_addr,
            'sms_info' : d.sms_info,
            "status" : d.status,
            'send_time' : d.send_time
        })
    return jsonify(data=datas)

@app.route("/add")
def add_user():
    ip_addr = '2.2.4.8'
    sms_info = "2019年9月30号测试了一条222"
    status = '0'
    send_time = '15315661'
    sms = M_SMS(
        ip_addr = ip_addr,
        sms_info = sms_info,
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
        'status' : sms.status,
        'send_time' : sms.send_time
    }
    return jsonify(data=result)

if __name__ == "__main__":
    app.run(debug=True)

