from settings import Settings

class GameStats():

    def __init__(self,settings:Settings):
        self.settings=settings
        self.game_activte=True
        self.rest_stats()
    
    def rest_stats(self):
        """""初始化游戏信息"""
        self.ship_left=self.settings.ship_limit    
