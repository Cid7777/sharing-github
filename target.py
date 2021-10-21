# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:08:07 2021

@author: Williams.Garrett
"""
import pygame

class Target:
    """A class to manage the ship."""
    
    def __init__(self, tg_game):
        """Initialize the ship and set its starting position."""
        self.screen = tg_game.screen
        self.settings = tg_game.settings
        self.screen_rect = tg_game.screen.get_rect()
        
        #Movement flag
        self.target_moving_right = False
        self.target_moving_left = False
        
        #Load the ship image and get its rect.
        self.image = pygame.image.load('target.bmp')
        self.rect = self.image.get_rect()
        
        #Start each new ship at the bottom center of the screen.
        self.rect.midtop = self.screen_rect.midtop
        
        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's x value, not the rect
        self.x += self.settings.target_speed * self.settings.target_direction
        
        #Update rect object from self.x
        self.rect.x = self.x
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def center_target(self):
        "Center the ship on the screen."
        
        self.rect.midtop = self.screen_rect.midtop
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        
