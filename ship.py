import pygame

class Ship():
    def __init__(self,screen,ai_setting):
        #初始化飞船设置起始位置
        self.screen = screen
        self.ai_setting = ai_setting
        #加载飞船图片并获取其外接矩形
        self.image = pygame.image.load('D:/python/image/吴军.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom-60
        
        #飞船属性中添加小数
        self.center = float(self.rect.centerx)
        
        #向右移动标志
        self.moving_right = False
        #向左移动标志
        self.moving_left = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_setting.ship_speed
        self.rect.centerx = self.center
        
    def blitme(self):
        #在制定位置绘制飞船
        self.screen.blit(self.image,self.rect)