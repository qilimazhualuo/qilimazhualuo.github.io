import pygame
class GameStats():
    def __init__(self,ai_settings):
        #初始化信息
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ships_limit
        