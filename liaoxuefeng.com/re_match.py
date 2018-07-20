#!/usr/bin/env python3
#-*- conding: utf-8 -*-

"""
正则表达式
"""

import re

def is_valid_email(addr):
    if re.match(r'^([a-zA-Z\.]+[0-9]?)@([a-z0-9]+\.com)$', addr):
        return True

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('emailaddress ok')


def name_of_email(addr):
    if '<' in addr:
        m = re.match(r'[\<]([a-zA-Z\s]+)([a-z]+)@[a-z]+.org', addr)
    else:
        m = re.match(r'([a-z]+)@[a-z]+.org', addr)
    return m.group(1)

# 测试:
#assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('email name ok')