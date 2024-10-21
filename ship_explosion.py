import pygame
from pygame.locals import *

class Ship_explosion(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship_explosion, self).__init__()

        #need to create a list of images for the sprte to work
        self.image = pygame.transform.scale(pygame.image.load("ship_explosion.jpeg"), 150, 150)
        self.rect = self.image.get_rect()