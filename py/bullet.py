import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self,ai_settings,screen,ship):
        #在飞船所处位置创建一个子弹对象
        super(Bullet,self).__init__()
        self.screen = screen
        #在0，0处创建一个子弹,并更改位置于飞船上端
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #用小数作为子弹位置
        self.y = float(self.rect.y)
        #子弹颜色
        self.color = ai_settings.bullet_color
        #子弹速度
        self.speed_factory = ai_settings.bullet_speed_factory
    
    def update(self):
        #更新子弹位置
        self.y -= self.speed_factory
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)