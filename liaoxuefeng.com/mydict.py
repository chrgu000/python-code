#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-06-28 16:05:43
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
说明
"""

class Dict(dict):
    """可以通过属性来访问的dict"""

    def __init__(self, **kw):
        """初始化属性"""
        super().__init__(**kw)

    def __getattr__(self, key):
        """得到属性"""
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Dict object has no attribute`%s" % key)

    def __setattr__(self, key, value):
        """设置属性"""
        self[key] = value
