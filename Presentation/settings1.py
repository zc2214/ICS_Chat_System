
class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.ship_speed=1.5
        self.ship_limit=3
        self.bullet_speed=1.0
        self.bullets_allowed = 10
        self.alien_speed= 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction=-1
        self.speedup_scale= 1.2
        self.score_scale=1.5
        self.initialize_dynamic_settings()