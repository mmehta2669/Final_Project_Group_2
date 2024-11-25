import pygame
from pygame.locals import *
from space_rubble import *

class game_level():
    def __init__(self):
        #pygame.init()
        #self.font = pygame.font.SysFont("georgia", 64, True)
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






        
