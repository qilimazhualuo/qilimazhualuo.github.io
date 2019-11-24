import sys
import pygame
from bullet import Bullet

def check_event(ship,ai_setting,screen,bullets):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_event_keydown(event,ship,ai_setting,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_event_keyup(event,ship)

def check_event_keydown(event,ship,ai_setting,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullet)
    
def check_event_keyup(event,ship):   
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def update_screen(ai_setting,screen,ship,bullets):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()