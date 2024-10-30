
class space_rubble:
    from typing import Any
import pygame
from pygame.locals import *
import random

screen_width = 770
screen_height = 570

class Space_rubble(pygame.sprite.Sprite):
    def __init__(self):
        super(Space_rubble, self).__init__()  
        self.image = pygame.transform.scale(pygame.image.load("rock.png"), (100, 100))
        
        self.start_horizontal_left = random.randint(-50, -10)
        self.start_horizontal_right = random.randint(screen_width + 10, screen_width + 50)        
        self.start_points = (self.start_horizontal_left, self.start_horizontal_right)

        self.start_horizontal = random.choice(self.start_points)
        self.start_vertical = random.randint(0, screen_height)

        self.rect = self.image.get_rect(                
            center = (
                self.start_horizontal,
                self.start_vertical               
            )            
        )

        self.speed = 1
        
    def update(self):
        if self.start_horizontal > 0:
            self.rect.move_ip(-self.speed, 0)
            if self.start_horizontal > 0 and self.rect.right < 0:
                self.rect = self.image.get_rect(
                    center = (
                self.start_horizontal,
                self.start_vertical               
            ) 
                )
        elif self.start_horizontal < 0:
            self.rect.move_ip(self.speed, 0)
            if self.start_horizontal < 0 and self.rect.left > screen_width:
                self.rect = self.image.get_rect(
                    center = (
                        self.start_horizontal,
                        self.start_vertical
                    )
                )

    def hit(self):
        self.kill()

