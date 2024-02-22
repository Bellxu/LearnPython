import pygame
from pygame.sprite import  Sprite


class Alien(Sprite):
    def __init__(self,settings,screen):
        super(Alien, self).__init__()
        """初始化外星人的位置"""
        self.screen=screen
        self.seetings=settings
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        """""外星人初始化在左上角"""
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #存储外星人的准确位置
        self.x=float(self.rect.x)

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.center-=self.seetings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.seetings.ship_speed_factor
        self.rect.centerx=self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)

