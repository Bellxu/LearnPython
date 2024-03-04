class Settings():
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        # self.bg_color=(0,0,255)
        self.bg_color=(233,233,255)
        #飞船相关
        self.ship_limit=3
        #子弹的属性
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=3
        #外星人相关
        self.alien_fleet_drop_speed=2

        self.game_speed_scale=1.1
        self.score_scale=1.5
        
        self.initialize_dynamic_settings()
        
    
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右；为-1表示向左
        #舰队方向
        self.alien_fleet_direction=-1
        self.aline_point=50

    def increase_speed(self):
        self.ship_speed_factor *= self.game_speed_scale
        self.bullet_speed_factor *= self.game_speed_scale
        self.alien_speed_factor *=self.game_speed_scale
        self.aline_point = int(self.aline_point * self.score_scale)
