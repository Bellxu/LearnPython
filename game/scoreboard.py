import pygame.ftfont
from pygame.surface import Surface
from game_stats import GameStats
from settings import Settings

class ScoreBoard():
    """""显示得分信息的类"""
    def __init__(self,screen :Surface,settings:Settings,game_stats:GameStats) -> None:
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.setting=settings
        self.stats=game_stats
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.prep_score()
    
    def prep_score(self):
        """""将得分转换为图像"""
        score_rounded=int(round(self.stats.score,-1))
        score_str="{:,}".format(score_rounded)
        self.score_image=self.font.render(score_str,True,self.text_color,self.setting.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
    
    def show_scre(self):
        """""在屏幕上显示计分板"""
        self.screen.blit(self.score_image,self.score_rect)