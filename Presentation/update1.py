class ICSGame():
    def run_game(self):
        while True:
            self.check_events()
            if self.stats.game_active:
                self.ship.update()
                self.update_bullets()  
                self.update_aliens()
            self.update_screen()
            #每次循环的时候都重新绘制屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()