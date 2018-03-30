#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-03-09 15:30:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
计分系统
"""

import pygame.font
import pygame.image

from pygame.sprite import Group
from ship import Ship
from kill_effect import KillEffect
from other_sprite import OtherSprite


class Scoreboard:
    """统计分数"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 默认分数对象
        self.num_source = str(0)

        # 外星人死亡的坐标、分数
        self.aline_dead_x = 0
        self.aline_dead_y = 0
        self.aline_dead_score = stats.score


        # 显示得分信息时使用的字体设置

        self.text_color = (240, 230, 140)
        self.font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 24, )

        # 显示得分数字时使用的图片文件
        self.num_file = ['images/num_%s.png' % x for x in range(10)]

        # 准备初始得分图像、最高分图像、等级图像、剩余飞船图像
        #self.prep_score()
        self.prep_score_new()  # 数字得分替换为图片
        #self.prep_high_score()
        self.prep_high_score_new()

        #self.prep_level()
        self.prep_level_new()
        self.prep_ships_left()
        self.prep_ships()

    def creat_socre_num_image(self):
        """将分数每个数字替换为相应数字的图片"""
        scores = Group()
        # 设置得分图片及属性
        num_figures = 0  # 位数，个位
        for x in str(self.num_source)[::-1]:
            score = OtherSprite()
            image_path = self.num_file[int(x)]
            score.image = pygame.image.load(image_path)
            score.rect = score.image.get_rect()
            num_figures += 1
            scores.add(score)
        return scores

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        self.rounded_score = round(self.stats.score, -1)
        score_str = u"得分: " + "{:,}".format(self.rounded_score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, )

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_score_new(self):
        """当前得分对应数字图片"""
        self.num_source = self.stats.score
        self.num_file = ['images/num_%s.png' % x for x in range(10)]
        self.scores = self.creat_socre_num_image()
        num_figures = 0
        for score in self.scores.sprites():
            score.rect.right = self.screen_rect.right - 20\
                    - score.rect.width * num_figures
            score.rect.top = 20
            num_figures += 1


    def prep_high_score(self):
        """将最高得分渲染成一副图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "最高分: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,
                True, (255,20,147), )
        # 将最商得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_high_score_new(self):
        """将最高得分渲染成一副图像"""
        self.num_source = self.stats.high_score
        self.num_file = ['images/num_%s_0.png' % x for x in range(10)]
        self.high_scores = self.creat_socre_num_image()
        # 将最高得分放在屏幕顶部中央
        #print("最高分长度：", len(self.high_scores))
        high_scores_nums = len(self.high_scores)
        num_figures = 0
        for high_score in self.high_scores.sprites():
            high_score.rect.centerx = int(self.screen_rect.centerx +\
                    (int(high_scores_nums / 2) * high_score.rect.width) -\
                    num_figures * high_score.rect.width)
            high_score.rect.top = self.screen_rect.top
            num_figures += 1

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render("等级: " + str(self.stats.level),
                 True, self.text_color,)
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20  # 位置
        self.level_rect.top = 150  # 位置

    def prep_level_new(self):
        """新的等级图像"""
        self.num_source = self.stats.level
        self.num_file = ['images/num_%s_0.png' % x for x in range(10)]
        self.levels = self.creat_socre_num_image()
        num_figures = 0
        for level in self.levels.sprites():
            for score in self.scores.sprites():
                score_bottom = score.rect.bottom
            level.rect.top = score_bottom + 20
            level.rect.right = self.screen_rect.right - 20 -\
                    level.rect.width * num_figures
            num_figures += 1
        self.prep_level_name()

    def prep_level_name(self):
        """LEVEL的英文图像"""
        self.level_image = pygame.image.load('images/level.png')
        self.level_image_rect = self.level_image.get_rect()
        for level in self.levels.sprites():
            # srpites 从右往左取值
            level_top = level.rect.top
            level_left = level.rect.left
        self.level_image_rect.top = level_top
        self.level_image_rect.right = level_left - 10


    def prep_ships_left(self):
        """将等级转换为渲染的图像"""
        self.ships_number_image = self.font.render(
                "飞船: " + str(self.stats.ships_left),
                 True, self.text_color,)
        # 将等级放在得分下方
        self.ships_number_rect = self.ships_number_image.get_rect()
        self.ships_number_rect.left = self.screen_rect.left + 20
        self.ships_number_rect.top = 20

    def prep_aline_point(self):
        """将击杀外星人的当前分数转换为渲染的图像"""
        self.aline_point_image = self.font.render(
                '+' + str(self.aline_dead_score),
                 True, self.text_color,)
        # 将等级放在得分下方
        self.aline_point_rect = self.aline_point_image.get_rect()
        self.aline_point_rect.x = self.aline_dead_x
        self.aline_point_rect.y = self.aline_dead_y


    def prep_ships(self):
        """显示还余下多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.ship_hp()
            ship.rect.x = 10 + ship_number * (ship.rect.width + 10)
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示得分"""
        #self.screen.blit(self.score_image, self.score_rect)
        #self.screen.blit(self.high_score_image, self.high_score_rect)
        #self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        #self.screen.blit(self.ships_number_image, self.ships_number_rect)


        #self.screen.blit(self.aline_point_image, self.aline_point_rect)


        # 绘制飞船、击杀得分
        self.ships.draw(self.screen)
        self.scores.draw(self.screen)
        self.high_scores.draw(self.screen)
        self.levels.draw(self.screen)
