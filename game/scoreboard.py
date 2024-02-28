import pygame.ftfont
from pygame.surface import Surface
from game_stats import GameStats
from settings import Settings
from ship import Ship
from pygame.sprite import Group

class ScoreBoard():
    """""显示得分信息的类"""
    def __init__(self,screen :Surface,settings:Settings,game_stats:GameStats) -> None:
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.setting=settings
        self.stats=game_stats
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont("SimHei",30)
        self.prep_score()
        self.prep_high_score()
        self.prep_game_level()
        self.prep_ships()
    
    def prep_ships(self):
        self.ships=Group()
        for ship_index in range(self.stats.ship_left):
            ship=Ship(self.screen,self.setting)
            ship.rect.x=10+ship_index*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)
    
    def prep_score(self):
        """""将得分转换为图像"""
        score_rounded=int(round(self.stats.score,-1))
        score_str="目前得分"+"{:,}".format(score_rounded)
        self.score_image=self.font.render(score_str,True,self.text_color,self.setting.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
        
    def prep_game_level(self):
        """""将游戏等级转换为图像"""
        game_level="level:"+str(self.stats.game_level)
        self.game_level_image=self.font.render(game_level,True,self.text_color,self.setting.bg_color)
        self.game_level_rect=self.game_level_image.get_rect()
        self.game_level_rect.right=self.score_rect.right
        self.game_level_rect.top=self.score_rect.bottom+10       
         
    def prep_high_score(self):
        """""将最高得分转换为图像"""
        high_score_rounded=int(round(self.stats.high_score,-1))
        high_score_str="最高得分"+"{:,}".format(high_score_rounded)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.setting.bg_color)
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top+15
        
    
    def show_score(self):
        """""在屏幕上显示计分板"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.game_level_image,self.game_level_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.ships.draw(self.screen)
        