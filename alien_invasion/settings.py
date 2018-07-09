#encoding:utf-8

class Settings():
    """存储《《外星人入侵》》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 1500
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_limit = 1      #3条命

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250, 60, 60
        self.bullet_allowed = 30     #限制子弹最大数量

        #外星人设置
        self.fleet_drop_speed = 10   #外星人竖直移动速度

        #以什么样的速度去加快游戏节奏
        self.speedup_scale = 1.2

        #外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而进行的设置'''
        self.ship_speed_factor = 2      # 飞船速度
        self.bullet_speed_factor = 3      # 子弹速度
        self.alien_speed_factor = 1       # 外星人水平移动速度

        # fleet_direction为1表示向右移， 为-1表示向左移
        self.fleet_direction = 1

        #记分
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度设置和外星人点数'''
        self.ship_speed_factor *=  self.speedup_scale
        self.bullet_speed_factor *=  self.speedup_scale
        self.alien_speed_factor *=  self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)