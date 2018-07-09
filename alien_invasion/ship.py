#encoding:utf-8

import pygame
import pygame.font

class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞船的位置'''
        #更改飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:      #确保飞船不会移出屏幕
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #根据self更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        #让飞船居中
        self.center = self.screen_rect.centerx

'''
    def show_end(self):
        # 在屏幕上显示game over:
        self.text_color3 = (30, 30, 30)
        self.font3 = pygame.font.SysFont(None, 48)
        self.image3 = self.font3.render("Game over", True, self.text_color3, self.ai_settings.bg_color)
        self.rect3 = self.image3.get_rect()
        self.rect3.top = 20
        self.rect3.left = 100
        self.screen.blit(self.image3, self.rect3)
        print("1")
'''


