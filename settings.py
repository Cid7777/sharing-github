# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:58:33 2021

@author: Williams.Garrett
"""

class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #Ship settings
        self.ship_speed = 2.0
        
        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 255)
        self.bullets_allowed = 1
        self.miss_chance = 3
        
        #Target settings
        self.target_speed = 2.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.target_direction = 1
        
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        "Initialize settings that change throughout the game."
        self.ship_speed = 2.0
        self.bullet_speed = 2.0
        self.target_speed = 2
        
        self.target_direction = 1
    
    def increase_speed(self):
        "Increase speed"
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale