import os
import sys
import cfg
import random
import pygame
from modules import *
 
 
'''开始游戏'''
def startGame(screen):
    clock = pygame.time.Clock()
    # 加载字体
    font = pygame.font.SysFont('arial', 18)
    if not os.path.isfile('score'):
        f = open('score', 'w')
        f.write('0')
        f.close()
    with open('score', 'r') as f:
        highest_score = int(f.read().strip())
    # 敌方
    enemies_group = pygame.sprite.Group()
    for i in range(55):
        if i < 11:
            enemy = enemySprite('small', i, cfg.WHITE, cfg.WHITE)
        elif i < 33:
            enemy = enemySprite('medium', i, cfg.WHITE, cfg.WHITE)
        else:
            enemy = enemySprite('large', i, cfg.WHITE, cfg.WHITE)
        enemy.rect.x = 85 + (i % 11) * 50
        enemy.rect.y = 120 + (i // 11) * 45
        enemies_group.add(enemy)
    boomed_enemies_group = pygame.sprite.Group()
    en_bullets_group = pygame.sprite.Group()
    ufo = ufoSprite(color=cfg.RED)
    # 我方
    myaircraft = aircraftSprite(color=cfg.GREEN, bullet_color=cfg.WHITE)
    my_bullets_group = pygame.sprite.Group()
    # 用于控制敌方位置更新
    # --移动一行
    enemy_move_count = 24
    enemy_move_interval = 24
    enemy_move_flag = False
    # --改变移动方向(改变方向的同时集体下降一次)
    enemy_change_direction_count = 0
    enemy_change_direction_interval = 60
    enemy_need_down = False
    enemy_move_right = True
    enemy_need_move_row = 6
    enemy_max_row = 5
    # 用于控制敌方发射子弹
    enemy_shot_interval = 100
    enemy_shot_count = 0
    enemy_shot_flag = False
    # 游戏进行中
    running = True
    is_win = False
    # 主循环
    while running:
        screen.fill(cfg.BLACK)
        for event in pygame.event.get():
            # --点右上角的X或者按Esc键退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # --射击
            if event.type == pygame.MOUSEBUTTONDOWN:
                my_bullet = myaircraft.shot()
                if my_bullet:
                    my_bullets_group.add(my_bullet)
        # --我方子弹与敌方/UFO碰撞检测
        for enemy in enemies_group:
            if pygame.sprite.spritecollide(enemy, my_bullets_group, True, None):
                boomed_enemies_group.add(enemy)
                enemies_group.remove(enemy)
                myaircraft.score += enemy.reward
        if pygame.sprite.spritecollide(ufo, my_bullets_group, True, None):
            ufo.is_dead = True
            myaircraft.score += ufo.reward
        # --更新并画敌方
        # ----敌方子弹
        enemy_shot_count += 1
        if enemy_shot_count > enemy_shot_interval:
            enemy_shot_flag = True
            enemies_survive_list = [enemy.number for enemy in enemies_group]
            shot_number = random.choice(enemies_survive_list)
            enemy_shot_count = 0
        # ----敌方移动
        enemy_move_count += 1
        if enemy_move_count > enemy_move_interval:
            enemy_move_count = 0
            enemy_move_flag = True
            enemy_need_move_row -= 1
            if enemy_need_move_row == 0:
                enemy_need_move_row = enemy_max_row
            enemy_change_direction_count += 1
            if enemy_change_direction_count > enemy_change_direction_interval:
                enemy_change_direction_count = 1
                enemy_move_right = not enemy_move_right
                enemy_need_down = True
                # ----每次下降提高移动和射击速度
                enemy_move_interval = max(15, enemy_move_interval-3)
                enemy_shot_interval = max(50, enemy_move_interval-10)
        # ----遍历更新
        for enemy in enemies_group:
            if enemy_shot_flag:
                if enemy.number == shot_number:
                    en_bullet = enemy.shot()
                    en_bullets_group.add(en_bullet)
            if enemy_move_flag:
                if enemy.number in range((enemy_need_move_row-1)*11, enemy_need_move_row*11):
                    if enemy_move_right:
                        enemy.update('right', cfg.SCREENSIZE[1])
                    else:
                        enemy.update('left', cfg.SCREENSIZE[1])
            else:
                enemy.update(None, cfg.SCREENSIZE[1])
            if enemy_need_down:
                if enemy.update('down', cfg.SCREENSIZE[1]):
                    running = False
                    is_win = False
                enemy.change_count -= 1
            enemy.draw(screen)
        enemy_move_flag = False
        enemy_need_down = False
        enemy_shot_flag = False
        # ----敌方爆炸特效
        for boomed_enemy in boomed_enemies_group:
            if boomed_enemy.boom(screen):
                boomed_enemies_group.remove(boomed_enemy)
                del boomed_enemy
        # --敌方子弹与我方飞船碰撞检测
        if not myaircraft.one_dead:
            if pygame.sprite.spritecollide(myaircraft, en_bullets_group, True, None):
                myaircr