#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-26 09:51:08
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
《外星人入侵》的设置模块
"""

class Settings:
    """存储《外星人入侵》的所有设置"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # 外星人的设置
        self.fleet_drop_speed = 20

        # 击杀得分移动速度设置
        self.kill_score_speed = 0.8

        # 外星人加速值
        self.speedup_scale = 1.1
        # 外星人点数的提高值
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.9
        self.bullet_speed_factor = 2.4
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移，为-1时向左移
        self.fleet_direction = 1

        # 记分
        self.alien_points = 10

    def increase_speed(self):
        """提高速度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)