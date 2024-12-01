import pygame

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, position):
        super(PowerUp, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load("level_up.png"), (30, 30))
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)
