import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,screen,settings):
        super(Ship,self).__init__()
        """初始化飞船位置"""
        self.screen=screen
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        """""飞船放在屏幕底部中央"""
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_left=False
        self.moving_right=False
        self.seetings=settings
        self.center=float(self.rect.centerx)

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.center-=self.seetings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.seetings.ship_speed_factor
        self.rect.centerx=self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        self.center=self.screen_rect.centerx

