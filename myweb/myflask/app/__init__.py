#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import logging
from .config import config
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'accounts.login'
login_manager.login_message = ''
login_manager.login_message_category = 'info'
login_manager.session_protection = "strong"


def create_app(config_name):

    app = Flask(__name__,
                template_folder=config[config_name].TEMPLATE_PATH, static_folder=config[config_name].STATIC_PATH)

    app.config.from_object(config[config_name])  # 从当前文件中加载配置

    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    ######### 日志 #############
    # 日志文件夹位置
    rootLogger = logging.getLogger(__name__)
    # rootLogger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(config[config_name].LOG_PATH, encoding='UTF-8')
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    rootLogger.addHandler(handler)
    rootLogger.setLevel(logging.DEBUG)

    # 在开头引用 db 还没创建，会报错
    from main.urls import main as main_blueprint
    from accounts.urls import accounts as accounts_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(accounts_blueprint, url_prefix='/accounts')

    return app
