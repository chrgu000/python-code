#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#在python中，配置文件的属性必须大写，防止一些不必要的错误！
"""
配置文件
"""
import os, datetime
    

class Config(object):  # 默认配置
    DEBUG = False
    SECRET_KEY = os.urandom(64)

    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    # 模板、静态文件目录
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates').replace('\\', '/')
    STATIC_PATH = os.path.join(TEMPLATE_PATH, 'static').replace('\\', '/')
    # EXPORT_PATH = os.path.join(BASE_DIR, 'exports').replace('\\', '/')

    REMEMBER_COOKIE_DURATION = datetime.timedelta(hours=3)

    ##################################
    #    日志
    # 日志文件夹位置
    LOG_DIR = os.path.join(BASE_DIR, 'logs').replace('\\', '/')
    # 日志文件位置
    LOG_PATH = os.path.join(LOG_DIR, 'app.log').replace('\\', '/')

    ###################################
    #   数据库配置
    ###################################
    DB_MODE = '0'  # 数据库模式 0-文件  1-mysql

    if DB_MODE == '0':
        db_uri = 'sqlite:///../db/monitor.db'
    elif DB_MODE == '1':
        username = 'root'
        password = '123456'
        host = '127.0.0.1'
        port = '3306'
        database = 'monitor'

        import mysql.connector
        db_uri = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (username, password, host, port, database)

    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

config = {
    "dev" : DevConfig,
    "default" : Config
}