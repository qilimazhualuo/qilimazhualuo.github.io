import pygame
class Ship():
    def __init__(self,screen):
        """初始化程序"""
        self.screen = screen

        #加载飞船图像
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        screen_rect = screen.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将每艘飞船置于屏幕底部
        self.rect.bottom = screen_rect.bottom - 10
        self.rect.centerx = screen_rect.centerx

        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self,ai_settings):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += ai_settings.ship_speed_factory
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= ai_settings.ship_speed_factory
        self.rect.centerx =self.center
    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
