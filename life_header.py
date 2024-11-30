import pygame
from pygame.locals import*

class life_header(pygame.sprite.Sprite):
    def __init__(self, screen, x = 650, y = 25):
        super().__init__()
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load("ship_1.png"), (30, 30))
        self.lives = 3
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)

        # initial empty list for players lives and fill
        self.images = []
        for i in range(self.lives):
            self.images.append((self.image, (self.x, self.y)))
            self.x += 40

    # return current number of lives
    def get_lives(self):
        return len(self.images)
    
    # remove life from list of available lives
    def remove_life(self):
        if len(self.images) >= 1:
            self.images.pop()

    def draw(self):
        for image, position in self.images:
            self.screen.blit(image, position)


    