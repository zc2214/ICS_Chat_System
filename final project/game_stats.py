# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:49:07 2021

@author: 86136
"""

class GameStats:
    def __init__(self, ai_game):
        self.settings=ai_game.settings
        self.reset_stats()
        self.high_score = 0
        self.game_active= False
        
    def reset_stats(self):
        self.ships_left=self.settings.ship_limit
        self.score=0
        self.level=1