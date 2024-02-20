import pygame


class Ship():
    def __init__(self,screen,settings):
        """初始化飞船位置"""
        self.screen=screen
        self.image=pygame.image.load('images/ship.bmp')
        self.ret=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        """""飞船放在屏幕底部中央"""
        self.ret.centerx=self.screen_rect.centerx
        self.ret.bottom=self.screen_rect.bottom
        self.moving_left=False
        self.moving_right=False
        self.seetings=settings
        self.center=float(self.ret.centerx)

    def update(self):
        if self.moving_left and self.ret.left > 0:
            self.center-=self.seetings.ship_speed_factor
        if self.moving_right and self.ret.right < self.screen_rect.right:
            self.center+=self.seetings.ship_speed_factor
        self.ret.centerx=self.center

    def blitme(self):
        self.screen.blit(self.image,self.ret)

