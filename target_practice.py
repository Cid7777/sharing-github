# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:58:16 2021

@author: Williams.Garrett
"""

import pygame
from time import sleep


from settings import Settings
from ship import Ship
from bullet import Bullet
from target import Target
from game_stats import GameStats
from button import Button

class TargetPractice:
    
    def __init__(self):
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
                                               self.settings.screen_height))
        pygame.display.set_caption("Target Practice")
        
        
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pygame.sprite.Group()
        
        self.bg_color = (self.settings.bg_color)
        
        self.play_button = Button(self, "Play")
    
    def run_game(self):
        while True:
            self._check_events()
            
            if self.stats.game_active == True:
                self.ship.update()
                self._update_bullets()
                self._update_target()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
        elif event.key == pygame.K_p:
            if not self.stats.game_active:
                self._start_game()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()
            self.settings.initialize_dynamic_settings()
            
    def _check_bullet_target_collision(self):
        if pygame.sprite.spritecollideany(self.target, self.bullets):
            for bullet in self.bullets.copy():
                self.bullets.remove(bullet)
            self.settings.increase_speed()
    
    def _check_edges(self):
        if self.target.check_edges():
            self._change_target_direction()
            
    def _start_game(self):
        self.stats.reset_stats()
        self.stats.game_active = True
        
        pygame.mouse.set_visible(False)
        
        self.bullets.empty()
        
        self.target.center_target()
        self.ship.center_ship()
            
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _change_target_direction(self):
        self.settings.target_direction *= -1
    
    def _miss_shot(self):
        if self.stats.chances_left > 0:
            self.stats.chances_left -= 1
        
            sleep(0.5)
        else:
            self.stats.game_active =  False
            pygame.mouse.set_visible(True)
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.blitme()
        
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()
        
    def _update_bullets(self):
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
                self._miss_shot()

        self._check_bullet_target_collision()
    
    def _update_target(self):
        self._check_edges()
        self.target.update()
        
        
if __name__ == '__main__':
    tg = TargetPractice()
    tg.run_game()