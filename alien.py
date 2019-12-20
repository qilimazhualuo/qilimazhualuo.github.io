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