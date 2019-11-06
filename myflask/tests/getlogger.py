#!/usr/bin/env python
#-*- coding: UTF-8 -*-
# author:yao.yinfeng
# message: 日志记录模块
# 主要特性：1、单例模式，线程安全
#           2、按照日期备份文件

'''
使用示例：
from ...common import jfmlogging
logger = jfmlogging.JFMlogging().getloger()
logger.error("this is error msg")
logger.info("this is info msg")
logger.debug("this is debug msg")
'''
import os
import os.path
import socket
import logging
import logging.handlers


logging.basicConfig()

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class JFMlogging(object):
    log = None
    def __init__(self):
        HOST_NAME = socket.gethostname()
        IP = socket.gethostbyname(HOST_NAME)
        LOGGING_MSG_FORMAT = '[%(asctime)s] [' + HOST_NAME + '] [' + IP + '] [%(levelname)s] [%(module)s.py] [line:%(lineno)d] %(message)s'
        LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
        LOG_PATH = 'logs' # 日志存放目录
        print2console = True  # 是否输出到屏幕，默认（True）输出
        logging.basicConfig(level=logging.DEBUG,format=LOGGING_MSG_FORMAT,datefmt=LOGGING_DATE_FORMAT)
        self.log = logging.getLogger('JFM')
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)
        log_file = os.path.join(LOG_PATH,'jfm.log')
        logger = logging.handlers.TimedRotatingFileHandler(log_file,'midnight',1)
        logger.setFormatter(logging.Formatter(LOGGING_MSG_FORMAT))
        self.log.addHandler(logger)

        if print2console:
            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            console.setFormatter(logging.Formatter(LOGGING_MSG_FORMAT))
            self.log.addHandler(console)

    def getloger(self):
        return self.log