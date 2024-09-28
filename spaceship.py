from typing import Any
import math
import pygame
from pygame.locals import *


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()  
        self.image = pygame.transform.scale(pygame.image.load(image_path), (30, 30))  
        self.original_image = self.image
        self.rect = self.image.get_rect()  
        self.rect.center = (x, y)

        self.thrust = 0.1  # thrust increment per frame
        self.max_speed = 5
        self.speed = 0  # current speed
        self.rotation_speed = 3
        self.angle = 0

    
    def rotate(self):
        # rotate the ship image and update the rect
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)  # keep the center in the same place
        

    def update(self):
        keys = pygame.key.get_pressed()

        # rotate the ship based on arrow key inputs
        if keys[K_LEFT]:
            self.angle += self.rotation_speed
        if keys[K_RIGHT]:
            self.angle -= self.rotation_speed

        # Up arrow key thrusts forward
        if keys[K_UP]:
            # Calculate the velocity based on the ship's angle
            rad_angle = math.radians(self.angle)
            self.speed += self.thrust
            self.speed = min(self.speed, self.max_speed)
        else:
            self.speed *= 0.95
        
        rad_angle = math.radians(self.angle)
        self.rect.x -= math.sin(rad_angle) * self.speed
        self.rect.y -= math.cos(rad_angle) * self.speed

        self.rotate()


    def draw(self, screen):
        screen.blit(self.image, self.rect)
