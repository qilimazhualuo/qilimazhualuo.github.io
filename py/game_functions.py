import sys
import pygame
from bullet import  Bullet
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
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
def update_ship(ship,ai_settings):
    ship.update(ai_settings)
def get_number_aliens_x(ai_settings,alien_width):
    """"计算x方向容纳alien数量"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
    """"新建alien"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.y = row_number * alien_height * 2
    alien.rect.y = alien.y
    aliens.add(alien)
def create_fleet(ai_settings,screen,aliens):
    """创建一个外星人群"""
    #创建外星人
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = 3
    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings,screen,aliens,alien_number,row_number)
def check_fleet_edges(ai_settings,aliens):
    """"有外星人到达边缘时采取措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    """将整个外星人群向下移动"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
def update_aliens(ai_settings,aliens,ship,stats,bullets,screen):
    """"检查是否处于边缘，调整位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #检测外星人和飞船碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,aliens,bullets,ai_settings,screen,ship)
def ship_hit(stats,aliens,bullets,ai_settings,screen,ship):
    #飞船数量-1
    stats.ships_left -= 1
    print(stats.ships_left)
    #清空子弹和外星人
    aliens.empty()
    bullets.empty()
    #创建一群新的外星人，将飞船放置于中心
    create_fleet(ai_settings,screen,aliens)
    ship.center_ship()
    #暂停
    sleep(0.5)
def update_bullets(aliens,bullets,ai_setting,screen):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(bullets,aliens,ai_setting,screen)
def check_bullet_alien_collisions(bullets,aliens,ai_settings,screen):
    #检测子弹和外星人碰撞
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) <= 0:
        bullets.empty()
        create_fleet(ai_settings,screen,aliens)
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