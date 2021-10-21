#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, tg_game):
        """Initialize the ship and set its starting position."""
        self.screen = tg_game.screen
        self.settings = tg_game.settings
        self.screen_rect = tg_game.screen.get_rect()
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        
        #Load the ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        
        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Update rect object from self.x
        self.rect.x = self.x
        
    
    def center_ship(self):
        "Center the ship on the screen."
        
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        

