
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
        self.image = pygame.transform.rotate(self.image, random.randint(0, 360))
        
        # create random horizontal and vertical start points for rubble objects
        self.start_left_or_top = random.randint(-50, -10)
        self.start_right = random.randint(screen_width + 10, screen_width + 50)
        self.start_bottom = random.randint(screen_height + 10, screen_height + 50)

        self.start_top_bottom = (self.start_left_or_top, self.start_bottom)
        self.start_left_right = (self.start_left_or_top, self.start_right)

        self.start_horizontal = 0
        self.start_vertical = 0
        self.rect = self.image.get_rect(
            center = (
                0,0
            )
        )

        # randomly choose between top, bottom, left, and right for the start point of an asteroid
        self.start_top_side = ("top/bottom", "left/right")
        self.rand_start = random.choice(self.start_top_side)

        if self.rand_start == "top/bottom":
            self.start_horizontal = random.randint(100, screen_width - 100)
            self.start_vertical = random.choice(self.start_top_bottom)

            self.rect = self.image.get_rect(
                center = (
                    self.start_horizontal,
                    self.start_vertical
                )
            )

        elif self.rand_start == "left/right":
            self.start_horizontal = random.choice(self.start_left_right)
            self.start_vertical = random.randint(0, screen_height)

            self.rect = self.image.get_rect(                
                center = (
                    self.start_horizontal,
                    self.start_vertical               
                )               
            )

        # create random speeds for asteroids and sets speed at which asteroid object will move
        self.speed_options = (1, 1.3, 1.5, 1.8, 2)
        self.speed = random.choice(self.speed_options)

    def get_speed(self):
        return self.speed

    def increase_speed(self, speed):
        self.speed = speed

    # Define movement of asteroids    
    def update(self):
        # define movement for rubble starting to the right of the screen
        if self.start_horizontal > 0 and (self.start_vertical >= 0 and self.start_vertical <= screen_height):
            self.rect.move_ip(-self.speed, 0)
            if self.start_horizontal > 0 and self.rect.right < 0:
                self.rect = self.image.get_rect(
                    center = (
                self.start_horizontal,
                self.start_vertical               
            ) 
                )

        # define movement for rubble starting to the left of the screen        
        elif self.start_horizontal < 0 and (self.start_vertical >= 0 and self.start_vertical <= screen_height):
            self.rect.move_ip(self.speed, 0)
            if self.start_horizontal < 0 and self.rect.left > screen_width:
                self.rect = self.image.get_rect(
                    center = (
                        self.start_horizontal,
                        self.start_vertical
                    )
                )
        # define movement for rubble starting at the bottom of the screen
        elif self.start_vertical > 0 and (self.start_horizontal >=0 and self.start_horizontal <= screen_width):
            self.rect.move_ip(-1, -self.speed)
            if self.rect.bottom < 0:
                self.rect = self.image.get_rect(
                    center = (
                        self.start_horizontal,
                        self.start_vertical
                    )
                )

        # define movement for rubble starting at the top of the screen
        elif self.start_vertical < 0 and (self.start_horizontal >= 0 and self.start_horizontal <= screen_width):
            self.rect.move_ip(1, self.speed)
            if self.rect.top > screen_height:
                self.rect = self.image.get_rect(
                    center = (
                        self.start_horizontal,
                        self.start_vertical
                    )
                )

    def hit(self):
        self.kill()

