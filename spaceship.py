from typing import Any
import math
import pygame
from pygame.locals import *

from bullet import Bullet


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, screen_width, screen_height):
        super().__init__()  
        self.image = pygame.transform.scale(pygame.image.load(image_path), (30, 30))  
        self.original_image = self.image
        self.rect = self.image.get_rect()  
        self.rect.center = (x, y)

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.thrust = 0.03  # thrust increment per frame
        self.drag = 1.03
        self.max_speed = 2
        self.speed = 0  # current speed
        self.rotation_speed = 3
        self.angle = 0

        self.bullets = []
        self.bullet_speed = 5
        self.shoot_delay = 250
        self.last_shot_time = pygame.time.get_ticks()

        # Load bullet sound effect
        self.bullet_sound = pygame.mixer.Sound("bullet_shot.wav")  # Replace with the path to your sound file


    def rotate(self):
        # rotate the ship image and update the rect
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)  # keep the center in the same place
        
    def shoot(self):
        # Fire a bullet from the front of the ship
        now = pygame.time.get_ticks()
        if now - self.last_shot_time > self.shoot_delay:
            # Reset the time the last shot was made
            self.last_shot_time = now
            bullet = Bullet(self.rect.centerx, self.rect.centery, self.angle, self.bullet_speed)
            self.bullet_sound.play()
            self.bullets.append(bullet)


    def update(self):
        keys = pygame.key.get_pressed()

        # Rotate the ship based on arrow key inputs only if rotation is needed
        if keys[K_LEFT] or keys[K_RIGHT]:
            if keys[K_LEFT]:
                self.angle += self.rotation_speed
            if keys[K_RIGHT]:
                self.angle -= self.rotation_speed
            self.rotate()  # Rotate only if angle changes

        # Up arrow key thrusts forward
        if keys[K_UP]:
            # Calculate the velocity based on the ship's angle
            rad_angle = math.radians(self.angle)
            self.speed += self.thrust
            self.speed = min(self.speed, self.max_speed)
        else:
            self.speed /= self.drag

        rad_angle = math.radians(self.angle)
        self.rect.x -= math.sin(rad_angle) * self.speed
        self.rect.y -= math.cos(rad_angle) * self.speed

        # Ensure the ship doesn't go offscreen
        self.rect.clamp_ip(pygame.Rect(0, 0, self.screen_width, self.screen_height))


        # Shoot bullets when spacebar is pressed
        if keys[K_z]:
            self.shoot()
            
        # Update bullets
        for bullet in self.bullets:
            bullet.update()

        # Remove bullets that go off screen
        self.bullets = [bullet for bullet in self.bullets if 0 <= bullet.rect.x <= self.screen_width and 0 <= bullet.rect.y <= self.screen_height]


    def draw(self, screen):
        screen.blit(self.image, self.rect)

        for bullet in self.bullets:
            pygame.draw.rect(screen, (125, 249, 255), bullet.rect)