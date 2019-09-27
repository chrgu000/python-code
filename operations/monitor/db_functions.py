#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
操作数据库
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


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

data = M_SMS.query.all()
datas = []
for user in data:
    print("id=>>", user.id, 
        "ip_addr=>>", user.ip_addr,
        "sms_info=>>", user.sms_info,
        "status=>>", user.status,
        "send_time=>>", user.send_time
    )
