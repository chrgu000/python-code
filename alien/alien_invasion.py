#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-26 09:39:55
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
用模块pygame开发《外星人入侵》
"""

import pygame
from pygame.sprite import Group

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygeme、设置和屏幕对象
    pygame.init()

    # 加载设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个存储子弹的编组
    bullets = Group()
    # 创建一个外星人的编组
    aliens = Group()

    # 创建个星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建击杀编组
    kes = Group()


    #开始游戏的主循环
    while True:

        gf.check_events(ai_settings, screen, stats, sb,
                    play_button, ship, bullets, aliens)
        if stats.game_active:
            if stats.begin_first:
                stats.begin_first = False
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, kes,
                        ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            gf.update_kill_scores(kes)
        gf.update_screen(ai_settings, screen, stats, sb, kes,
                    ship, aliens, bullets, play_button)


run_game()
