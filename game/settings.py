class Settings():
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        # self.bg_color=(0,0,255)
        self.bg_color=(233,233,255)
        #飞船相关
        self.ship_speed_factor=1.5
        #子弹的属性
        self.bullet_speed_factor=1
        self.bullet_width=300
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=3
        #外星人相关
        self.alien_speed_factor=1

        self.alien_fleet_drop_speed=10
        #舰队方向
        self.alien_fleet_direction=1


