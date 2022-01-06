import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from button import Button
from scoreboard import Scoreboard
class AlienInvasion:
    """管理游戏资源和行为的类"""
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
        
    def run_game(self):
        """开启游戏主循环"""
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
            #让最近绘制的屏幕可见
    def check_events(self):
        """相应按键和鼠标事件"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self.check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_play_button(mouse_pos)
    def fire_bullet(self):
        """创建一颗子弹，并将其加入编组bulles中"""
        if len(self.bullets)< self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
                
                    
    def check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
            

    def check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False
                    
    def update_screen(self):
        """每次循环重新绘制屏幕并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
    def update_bullets(self):
         self.bullets.update()
         for bullet in self.bullets.copy():
             if bullet.rect.bottom<=0:
                 self.bullets.remove(bullet)
         self.check_bullet_alien_collisions()
    def check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score+=self.settings.alien_points*len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()
            self.settings.increase_speed()
            
            self.stats.level+=1
            self.sb.prep_level()
        
    def create_alien(self, alien_number, row_number):
         alien = Alien(self)
         alien_width, alien_height =alien.rect.size
         alien.x = alien_width + 2 * alien_width * alien_number
         alien.rect.x = alien.x
         alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
         self.aliens.add(alien)

    def create_fleet(self):
        """创建外星人群"""
        """创建一个外星人"""
        alien=Alien(self)
        self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        ship_height=self.ship.rect.height
        available_space_y=(self.settings.screen_height-(3*alien_height)-ship_height)
        number_rows=available_space_y // (2*alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)
    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
        self.check_aliens_bottom()
        
    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break
    
    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    def ship_hit(self):
        if self.stats.ships_left>0:
            self.stats.ships_left-=1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active=False
            pygame.mouse.set_visible(True)
            
        
        sleep(0.5)
    def check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break
    def check_play_button(self, mouse_pos):
        botton_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if botton_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active= True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
            self.aliens.empty()
            self.bullets.empty()
            
            self.create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
        

def main():
    ai=AlienInvasion()
    ai.run_game()
if __name__=='__main__':
    #创建游戏实例并运行游戏
    main()
