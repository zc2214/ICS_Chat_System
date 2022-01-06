
class Settings:
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        #飞船设置
        self.ship_speed=1.5
        self.ship_limit=3
        #子弹设置
        self.bullet_speed=1.0
        self.bullets_allowed = 10
       #外星人设置
        self.alien_speed= 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 1 表示右移 -1表示左移
        self.fleet_direction=-1
        self.speedup_scale= 1.2
        self.score_scale=1.5
        self.initialize_dynamic_settings()