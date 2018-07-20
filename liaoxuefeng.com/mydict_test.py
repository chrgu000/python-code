#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-06-28 16:17:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
对Dict模块进行单元测试
"""

import unittest

from mydict import Dict


class TestDict(unittest.TestCase):
    """测试Dict的所有属性"""
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
