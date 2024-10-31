import pygame
from pygame.locals import *
from space_rubble import *

class game_level():
    def __init__(self):
        self.rubble = pygame.sprite.Group()
        self.rubble_max = 5    

    def get_rubble(self):
        return self.rubble
    
    def get_max_rubble(self):
        return self.rubble_max
    
    def set_max_rubble(self):
        self.rubble_max = self.rubble_max * 2

    def next_level(self):
        self.rubble_max += 1
        
