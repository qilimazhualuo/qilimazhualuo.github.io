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
        if len(bullets) < ai_settings.max_account:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def creat_alien(ai_setting,screen,):
    '''创建一个外星人并放置在当前行'''
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien.rect.width + alien_number * alien.rect.width * 2
    alien.rect.x = alien.x
    aliens.add(alien)
def aaaa
def create_fleet(ai_settings,screen,aliens):
    """创建一个外星人群"""
    #创建外星人
    alien = Alien(ai_settings,screen)
    alien.width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien.width
    number_aliens_x = int(available_space_x / (2 * alien.width))
    #创建第一行外星人
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings,screen)
        alien.x = alien.rect.width + alien_number * alien.rect.width * 2
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
    #让最近绘制的屏幕可见
    pygame.display.flip()