import math
import pygame
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y, angle, speed):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((125, 249, 255))
        self.rect = self.image.get_rect(center=(x,y))

        # Set velocity based on the angle
        rad_angle = math.radians(angle)
        self.dx = -math.sin(rad_angle) * speed
        self.dy = -math.cos(rad_angle) * speed


    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        