import math
import pygame
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, screen, x, y, angle, speed, color, size):
        super().__init__()
        # Create the base image for the bullet
        self.original_image = pygame.Surface(size, pygame.SRCALPHA)  # Use SRCALPHA for transparency
        self.original_image.fill(color)  # Set the bullet color

        # Rotate the bullet to match the angle
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=(x, y))
        self.screen = screen

        # Set velocity based on the angle
        rad_angle = math.radians(angle)
        self.dx = -math.sin(rad_angle) * speed
        self.dy = -math.cos(rad_angle) * speed

    def update(self):
        # Move bullet based on velocity
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self):
        # Blit the rotated image onto the screen at the bullet's current position
        self.screen.blit(self.image, self.rect)
