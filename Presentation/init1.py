class ICSGame:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Have a rest after coding !')
        self.settings=Settings()
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        self.stats = GameStats(self)
        self.sb=Scoreboard(self)
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self.create_fleet()
        self.play_button = Button(self, 'play')
