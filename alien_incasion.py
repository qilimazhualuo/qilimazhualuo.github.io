import sys
import pygame
from setting import Setting
from ship import Ship
from alien import Alien
import game_functions as gf 
from pygame.sprite import Group

def run_game():
    #初始化游戏
    pygame.init()
    #创建一个屏幕并命名窗口
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien_invastion")
    #创建一艘飞船&子弹编组&外星人编组
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    #创建一个外星人
    gf.creat_fleet(ai_settings,screen,aliens)
    #开始游戏主循环
    while True:
        #执行操作
        gf.check_events(ship,ai_settings,screen,bullets)
        ship.update(ai_settings)
        #绘制屏幕
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)
        gf.update_screen(screen,ai_settings,ship,bullets,aliens)

run_game()