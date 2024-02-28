import pygame
from pygame.sprite import  Sprite
from settings import Settings
from pygame.surface import Surface


class Alien(Sprite):
    def __init__(self,settings:Settings,screen:Surface):
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
        self.last_time=pygame.time.get_ticks()

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def check_edges(self):
        if self.rect.right >self.screen.get_rect().right:
            return True
        elif self.rect.left <0:
            return True
        
    def update(self):
        current_time = pygame.time.get_ticks()
        # if(self.last_time==0):
        #     self.last_time=current_time
        #     self.x +=(self.seetings.alien_speed_factor * self.seetings.alien_fleet_direction)
        #     self.rect.x=self.x
        print("current_time ="+str(current_time)+"last_time"+str(self.last_time))
        if current_time-self.last_time >20:
            self.last_time=current_time
            self.x +=(self.seetings.alien_speed_factor * self.seetings.alien_fleet_direction)
            self.rect.x=self.x
        



