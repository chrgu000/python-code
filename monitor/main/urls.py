#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
路由
"""

from flask import Blueprint, g

from . import url_functions as uf

main = Blueprint('main', __name__)

main.add_url_rule("/all",  view_func=uf.all_data)
main.add_url_rule('/hello/<username>', view_func=uf.hello, methods=['POST', 'GET'])
main.add_url_rule('/hello', view_func=uf.hello, methods=['POST', 'GET'])