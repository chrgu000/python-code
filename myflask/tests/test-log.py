# -*- coding:utf-8 -*-
from flask import Flask
from getlogger import JFMlogging

app = Flask(__name__)
 
logger = JFMlogging().getloger()

@app.route('/')
def hello_world():
    logger.debug("测试打印日志")
    logger.warning("warning")
    logger.error("error")
    logger.fatal("fatal")
    return 'Hello, World!'
 
if __name__ == '__main__':
    app.debug = True
    app.run()