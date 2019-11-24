import sys
import pygame
from setting import Setting
from ship import Ship
import game_function as gf
from bullet import Bullet
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("吴军打飞机")
    ship = Ship(screen,ai_setting)

    bullets = Group()

    while True:
        gf.check_event(ship,ai_setting,screen,bullets)
        ship.update()
        bullets.update()

        

        gf.update_screen(ai_setting,screen,ship,bullets)
    
run_game()
