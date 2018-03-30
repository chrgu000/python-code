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

    def __init__(self, ai_settings, screen, stats, sb, kes):
        """初始化属性"""
        super().__init__()

        self.ai_settings = ai_settings
        self.screen = screen
        self.stats = stats
        self.sb = sb
        self.kes = kes

        # 设置显示内容
        self.text_color = sb.text_color
        self.font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 36, )
        #self.image = self.font.render(str(self.ai_settings.alien_points),
        #        True, self.text_color, )
        self.image = pygame.image.load('images/defen.png')

        # 设置属性、精确位置
        self.rect = self.image.get_rect()
        self.rect.x = float(self.rect.x)
        self.rect.y = float(self.rect.y)

    def check_edges(self):
        """如果击杀到达位置，就返回True"""
        # 得分数字图替换图片后失效
        #print(self.rect.x, self.sb.score_rect.left, "如果击杀到达位置，就返回True")
        if self.rect.x >= self.sb.score_rect.left and\
                self.rect.y <= self.sb.score_rect.bottom:
            return True

    def update(self):
        """更新击杀得分的位置"""
        score_center = (self.ai_settings.screen_width, 0)
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

        # 得分数字图替换为图片后修改
        # 检查碰撞，保留得分，清除击杀得分特效
        collisions = pygame.sprite.groupcollide(self.sb.scores, self.kes,
                        False, True)
        # 特效到达位置后更新得分
        if collisions:
            for kes in collisions.values():
                self.stats.score += self.ai_settings.alien_points * len(kes)
                self.sb.prep_score_new()