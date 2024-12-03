import pygame
from pygame.locals import *

class PauseMenu:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("georgia", 64, True)
        self.button_font = pygame.font.SysFont("Arial", 24)
        self.resume_rect = pygame.Rect(350, 300, 100, 50)
        self.exit_rect = pygame.Rect(350, 400, 100, 50)
        self.title = "Paused"
        self.score = "Score: "
        self.ended = False

    def show(self, screen, score, test) -> bool:
        screen.fill((0, 0, 0))  # Fill the screen with black
        
        #Draw the title
        title = self.font.render(self.title, True, (255, 255, 255))  
        title_rect = title.get_rect(center=(400, 150))  
        screen.blit(title, title_rect)  
        
        #Draw the score
        scoretxt = self.font.render((self.score + str(score)), True, (255, 255, 255))  
        score_rect = scoretxt.get_rect(center=(400, 250))  
        screen.blit(scoretxt, score_rect)  

        # Draw the resume button
        pygame.draw.rect(screen, (255, 0, 0), self.resume_rect)
        resume_text = self.button_font.render("Resume", True, (255, 255, 255))
        resume_text_rect = resume_text.get_rect(center=self.resume_rect.center)
        screen.blit(resume_text, resume_text_rect)
        
        # Draw the exit button
        pygame.draw.rect(screen, (255, 0, 0), self.exit_rect)
        button_text = self.button_font.render("Exit", True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=self.exit_rect.center)
        screen.blit(button_text, button_text_rect)

        pygame.display.flip() 

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.resume_rect.collidepoint(event.pos):
                        waiting = False        
                    elif self.exit_rect.collidepoint(event.pos):
                        waiting = False
                        self.ended = True
        if test == True:    
            pygame.quit()
        return self.ended