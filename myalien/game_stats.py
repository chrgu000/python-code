#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-07 16:24:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
用于跟踪游戏统计信息
"""
import json


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 游戏启动第一次开始
        self.begin_first = True

        # 任何情况下都不应该重围最高得分
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """读取最高分"""
        filename = 'score.json'
        try:
            with open(filename) as f_obj:
                high_score = json.load(f_obj)
        except FileNotFoundError:
            high_score = 0

        return high_score