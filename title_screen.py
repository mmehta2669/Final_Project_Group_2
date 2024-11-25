import pygame
from pygame.locals import *

class TitleScreen:
    def __init__(self, text):
        pygame.init()
        self.font = pygame.font.SysFont("georgia", 64, True)
        self.button_font = pygame.font.SysFont("Arial", 24)
        self.button_rect = pygame.Rect(350, 400, 100, 50)
        self.text = text

    def show(self, screen):
        screen.fill((0, 0, 0))  # Fill the screen with black
        text = self.font.render(self.text, True, (255, 255, 255))  # Render the title text
        text_rect = text.get_rect(center=(400, 150))  # Get the rect of the text
        screen.blit(text, text_rect)  # Blit the text onto the screen

        # Draw the button
        pygame.draw.rect(screen, (255, 0, 0), self.button_rect)
        button_text = self.button_font.render("Start", True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        screen.blit(button_text, button_text_rect)

        pygame.display.flip()  # Update the display

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        waiting = False