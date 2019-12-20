class Setting():
    def __init__(self):
        #初始化游戏

        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (226, 106, 106)
        #飞船速度
        self.ship_speed_factory = 0.4
        #子弹设置
        self.bullet_speed_factory = 0.2
        self.bullet_width = 3
        self.bullet_height = -10
        self.bullet_color = (192, 57, 43)
        self.max_account = 10