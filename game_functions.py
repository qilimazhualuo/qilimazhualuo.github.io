import sys
import pygame
from bullet import  Bullet
from bullet import Bullet
from alien import Alien

def check_events(ship,ai_settings,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ship,ai_settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
def check_keydown_event(event,ship,ai_settings,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < 3:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def creat_fleet(ai_settings,screen,aliens):
    """创建外星人群"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))

    #创建第一行外星人
    for ailen_number in range(number_aliens_x):
        alien = Alien(ai_settings,screen)
        alien.x = alien_width = 2*alien_width*ailen_number
        alien.rect.x = alien.x
        aliens.add(alien)

def update_screen(screen,ai_settings,ship,bullets,aliens):
    #重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    aliens.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()