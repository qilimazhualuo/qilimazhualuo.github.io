import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人类"""
    def __init__(self,ai_settings,screen):
        """初始化设置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图片
        self.image = pygame.image.load("images/timg.png")
        self.rect = self.image.get_rect()

        #设置外星人位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def check_edges(self):
        """若碰到边缘返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        """向右移动外星人位置"""
        self.x += (self.ai_settings.alien_speed_factory * self.ai_settings.fleet_direction)
        self.rect.x = self.x
    