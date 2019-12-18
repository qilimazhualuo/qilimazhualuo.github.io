import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,screen,ai_settings):
        super(Alien,self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图片，定义Rect
        self.image = pygame.image.load("images/timg.png")
        self.rect = self.image.get_rect()

        #定义外星人初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #使用浮点数存储外星人位置
        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
