#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-14 10:37:29
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
击杀外星人得分显示
"""
import pygame.font

from pygame.sprite import Sprite


class KillEffect(Sprite):
    """击杀后显示的类"""

    def __init__(self, ai_settings, screen, sb, kes):
        """初始化属性"""
        super().__init__()

        self.ai_settings = ai_settings
        self.screen = screen
        self.sb = sb
        self.kes = kes

        # 设置显示内容
        self.text_color = (255, 30, 30)
        self.font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 36, )
        self.image = self.font.render(str(sb.aline_dead_score),
                True, self.text_color, self.ai_settings.bg_color)
        # 设置属性、精确位置
        self.rect = self.image.get_rect()
        self.rect.x = float(self.rect.x)
        self.rect.y = float(self.rect.y)

    def check_edges(self):
        """如果击杀到达位置，就返回True"""
        #print(self.rect.x, self.sb.score_rect.left, "如果击杀到达位置，就返回True")
        if self.rect.x >= self.sb.score_rect.left and\
                self.rect.y <= self.sb.score_rect.bottom:
            return True

    def update(self):
        """更新击杀得分的位置"""
        score_center = self.sb.score_rect.midright
        kill_score_center = self.rect.center
        move_range = (abs(score_center[0] - kill_score_center[0]),
                    abs(score_center[1] - kill_score_center[1]))
        if move_range.index(max(move_range)):
            if self.rect.x < score_center[0]:
                self.rect.x += self.ai_settings.kill_score_speed
            if self.rect.y > score_center[1]:
                self.rect.y -= self.ai_settings.kill_score_speed *\
                        move_range[1]/move_range[0]
        else:
            if self.rect.x < score_center[0]:
                self.rect.x += self.ai_settings.kill_score_speed *\
                        move_range[0]/move_range[1]
            if self.rect.y > score_center[1]:
                self.rect.y -= self.ai_settings.kill_score_speed

        #if self.rect.x >= self.sb.score_rect.bottom:
            #self.text_color = self.ai_settings.bg_color
