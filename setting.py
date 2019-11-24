class Setting():
    #存储设置类
    def __init__(self):
        #初始化游戏设置
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        
        #子弹
        self.bullet_speed = 1
        self.bullet_width = 1
        self.bullet_height = 3
        self.bullet_color = 60,60,60