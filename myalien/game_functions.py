#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-02-26 11:28:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
"""
说明:
    重构代码，精简主文件内容
"""

import sys
import json
from time import sleep

import pygame

import random

from alien import Alien
from bullet import Bullet

from kill_effect import KillEffect


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多个行外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height))
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可以容纳几个个星人"""
    # 计算一行可容纳多少个
    # 外星人间距为外星人宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并放置在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,
                                    ship.rect.height,
                                    alien.rect.height,
                                )

    # 创建外星人群
    for row_number in range(number_rows):
        # 创建第一行外星人
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)

    # 随机删除外星人
    for alien in aliens:
        if random.randint(0, 1):
            aliens.remove(alien)


def check_keydown_events(event, ai_settings, screen,
                             stats, ship, bullets, aliens):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if stats.game_active:
            fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, sb ,ship, aliens, bullets)

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有达到上限，就发射一颗子弹"""
    # 创建一子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_events(ai_settings, screen, stats, sb,
        play_button, ship, bullets, aliens):
    """响应鼠标和键盘事件"""
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 关闭窗口退出程序
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen,
                             stats, ship, bullets, aliens)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, sb, ship, aliens, bullets,
                        stats, play_button, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, sb, ship, aliens, bullets,
                        stats, play_button, mouse_x, mouse_y):
    """玩家单击play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 重置游戏设置
    ai_settings.initialize_dynamic_settings()
    # 隐藏光标
    pygame.mouse.set_visible(False)
    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True
    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    #sb.prep_ships_left()
    sb.prep_ships()

    # 清空外星人列表和子弹编组
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人，并让飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, kes,
                    ship, aliens, bullets, play_button):
    """屏幕刷新"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    kes.draw(screen)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # 运行游戏首次点击play按钮前不显示外星人
    if stats.begin_first:
        pass
    else:
        aliens.draw(screen)
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    kes.update()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, kes, ship, aliens, bullets):
    """更新子弹的位置，删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查是否有子弹击中了外星人
    # 击中后就删除相应的子弹和外星人
    #collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    """
    collisions 遍历编组bullets中的每颗子弹，再遍历编组aliens中的每个外星人，
    每当有子弹和外星人的rect重叠时，groupcollide()就在它返回的字典中添加一个
    键-值对。第一个实参True告诉Pygame删除发生碰撞的子弹，第二个True删除外星人

    """
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, kes, ship,
                    aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, kes, ship,
                    aliens, bullets):
    """响应子弹和外星人发生碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            sb.aline_dead_score = sb.rounded_score
            stats.score += ai_settings.alien_points * len(aliens)
            sb.kill_scores_numbers = len(aliens)
            sb.prep_score()
            sb.aline_dead_score = sb.rounded_score - sb.aline_dead_score
            # 消灭的外星坐标
        for aline in aliens:
            #print(aline.rect.center, sb.aline_dead_score, end= '|||')
            #print(aline.rect.center)
            sb.aline_dead_x, sb.aline_dead_y = aline.rect.center
            sb.prep_aline_point()
            creat_kill_scores(ai_settings, screen, sb, kes)
            #sb.prep_kill_scores()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 外星人杀完后删除现有的子弹并新建一群外星人
        bullets.empty()  # 清空子弹
        #kes.empty()  # 清空击杀得分图像
        # 加快游戏节奏
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        #sb.aline_dead_score = ai_settings.alien_points

        create_fleet(ai_settings, screen, ship, aliens)

def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘，并更新整群外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    # 检测飞船是否到达底端
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """响应外星人撞到飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1
        #sb.prep_ships_left()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建新的外星人群，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """检查是否有外得人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样处理
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
    # 最高分存入文件
    with open('score.json', 'w') as f_obj:
        json.dump(stats.high_score, f_obj)

def creat_kill_scores(ai_settings, screen, sb, kes):
    """创建一个击杀得分图"""
    kill_scores = KillEffect(ai_settings, screen, sb, kes)
    kill_scores.rect.x = sb.aline_dead_x
    kill_scores.rect.y = sb.aline_dead_y
    kes.add(kill_scores)

def check_alien_kill_scores_collisions(ai_settings, sb, kes):
    """击杀得分碰撞消失"""
    # 删除到达位置的得分
    for ke in kes.sprites():
        if ke.rect.top >= sb.score_rect.bottom:
            print("到达1")
            kes.remove(ke)

def update_kill_scores(kes):
    """检查击杀效果是否到达位置，并更新"""
    for ke in kes.sprites():
        if ke.check_edges():
            kes.remove(ke)
    #print(len(kes))
    kes.update()
