import pygame
from pygame.locals import *
from space_rubble import *

class GameLevel():
    def __init__(self):
        self.font = pygame.font.SysFont("georgia", 64, True)
        self.max_rubble = 5
        self.rubble_count = 0
        self.level = 1
        self.speed = 1.5        

    # creates new enemy object that will be added to the game screen
    def get_new_rubble(self):    
        if self.level == 1:
            self.new_rubble = Space_rubble()
            return self.new_rubble
        else:
            self.new_rubble = Space_rubble()
            self.new_rubble.increase_speed(self.speed)
            return self.new_rubble
    
    def get_max_rubble(self):
        return self.max_rubble
    
    def get_rubble_count(self):
        return self.rubble_count
    
    def set_rubble_count(self):
        self.rubble_count += 1
    
    # advances the game to the next level, increasing difficulty
    def next_level(self):
        self.max_rubble *= 2
        self.rubble_count == 0
        self.level += 1
        self.speed *= 1.1

    # display level cleared text 
    def display_text(self):
        self.level_cleared_text = "Level " + "Cleared!"
        level_cleared_text = self.font.render(self.level_cleared_text, True, (255, 255, 255))
        level_cleared_rect = level_cleared_text.get_rect(center=(400, 300))
        return level_cleared_text, level_cleared_rect

        
    






        
