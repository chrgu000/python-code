#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-16 16:19:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
通用精灵
"""

import pygame


from pygame.sprite import Sprite


class OtherSprite(Sprite):
    """通用的精灵类"""

    def __init__(self):
        """初始化属性"""
        super().__init__()

        self.filepath = 'images/num_0.png'
        self.image = pygame.image.load(self.filepath)
        self.rect = self.image.get_rect()
