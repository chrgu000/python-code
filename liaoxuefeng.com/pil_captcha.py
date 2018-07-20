#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
通过PIL提供的ImageDraw生成字母验证码图片
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random


# 随机字母
def rndChar():
    s = [chr(random.randint(65,90)), chr(random.randint(97,122)), chr(random.randint(48,57))]
    return s[random.randint(0,2)]

# 随机颜色1
def rndColor():
    return (random.randint(80, 255), random.randint(80, 255), random.randint(80, 255), )

# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127), )

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255,255,255))
#创建Font对象
font = ImageFont.truetype('arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y), fill=rndColor())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
