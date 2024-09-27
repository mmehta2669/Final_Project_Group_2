from typing import Any
import pygame
from pygame.locals import *

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()  
        self.image = pygame.transform.scale(pygame.image.load(image_path), (30, 30))  
        self.rect = self.image.get_rect()  
        self.rect.x = x  
        self.rect.y = y  

    def update(self):
        pass  

    def draw(self, screen):
        screen.blit(self.image, self.rect)