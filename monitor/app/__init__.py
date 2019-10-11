#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from flask import Flask

db = SQLAlchemy()

def creat_app():
    app = Flask(__name__)

    # 连接mysql数据库
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost:3306/monitor'
    # 保存在本地sqlite文件中
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/monitor.db'
    # 不配置track会报错
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    # 在开头引用 db 还没创建，会报错    
    from main.urls import main as main_blueprint 
    app.register_blueprint(main_blueprint)

    return app

