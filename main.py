import pygame
import background
import spaceship
from spaceship import*
import space_rubble
from space_rubble import*
from pygame.locals import *
 
# Basic Starting Class
class App:
    
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.weight, self.height = 800, 600
        background_image = pygame.image.load("starysky.png")
        self.background = pygame.transform.scale(background_image, self.size)
        self.ship = None

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.player = Spaceship('ship.png', 400, 300)
        self.rubble = Space_rubble('rock.png', 230, 100)
        self._running = True
 

    
    # Basic Game Loop Functions
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            
    def on_loop(self):
        self.player.update()
        self.rubble.update()

        
        
    def on_render(self):
        # Clear the screen by filling it with the background
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        self.rubble.draw(self.screen)
        pygame.display.flip()
    
    
    def on_cleanup(self):
        pygame.quit()
 

    # The excute block which runs the loop reners an cleanup
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()