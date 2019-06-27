# -*- coding: utf-8 -*-
import re


w = "Blockchain wallet, a right vested in everyone. A private key is an asset. Please back it up twice."
re_en="[A-Za-z ]+"

print(re.findall(re_en, w))