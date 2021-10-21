#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 21:41:16 2021

@author: garrettwilliams
"""

class GameStats:
    "Track statistics for Alien Invasion."
    def __init__(self, tg_game):
        "Initialize statistics."
        self.settings = tg_game.settings
        self.reset_stats()
        
        #Start Alien Invasion in an inactive state for Play button.
        self.game_active = False
        
    def reset_stats(self):
        "Initialize statistics that can change during the game."
        self.chances_left = self.settings.miss_chance
        