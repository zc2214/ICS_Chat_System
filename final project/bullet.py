import pygame
from pygame.sprite import Sprite
from settings import Settings
class Bullet(Sprite):
    """管理飞船发射的子弹类"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
     


        #在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.image=pygame.image.load('images/bullet.png')
        self.rect=self.image.get_rect()
        
        
        self.rect.midtop=ai_game.ship.rect.midtop

        #储存用小数表示子弹位置

        self.y=float(self.rect.y)
    
    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -=self.settings.bullet_speed
        #更新表示子弹rect位置
        self.rect.y=self.y
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        '''
        pygame.draw.rect(self.screen,self.color ,self.rect)
        '''
        self.screen.blit(self.image, self.rect)
