#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
数据库
"""
from app import db

class M_SMS(db.Model):
    __tablename__ = 'm_sms'

    id = db.Column(db.Integer, primary_key=True)
    ip_addr = db.Column(db.String(15), nullable=False)
    sms_info = db.Column(db.Text, nullable=False)
    re_mobile = db.Column(db.String(15), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    send_time = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'host %r' % self.ip_addr


