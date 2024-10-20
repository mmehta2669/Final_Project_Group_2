import pygame
import background
import spaceship
from spaceship import*
from space_rubble import*
from ship_explosion import *
from game_level import *
from pygame.locals import *
 
# Basic Starting Class
class App:
    
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 800, 600
        background_image = pygame.image.load("starysky.png")
        self.background = pygame.transform.scale(background_image, self.size)
        self.ship = None

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.player = Spaceship('ship.png', 400, 300, screen_width=770, screen_height=570)
        self.level = game_level()

        #create asteroid event group and add player 
        self.add_rubble = pygame.USEREVENT + 1
        pygame.time.set_timer(self.add_rubble, 1500)

        self.rubble = pygame.sprite.Group()
        self.all_items = pygame.sprite.Group()
        self.all_items.add(self.player)

        self.rubble_count = 0
        self.max_rubble = self.level.get_max_rubble()

        self._running = True    
   
     
    # Basic Game Loop Functions
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == self.add_rubble: 
            self.new_rubble = Space_rubble()  
            if self.rubble_count < self.max_rubble: 
                self.rubble.add(self.new_rubble)
                self.all_items.add(self.new_rubble)
            if self.rubble_count != self.max_rubble:
                self.rubble_count += 1
                print(self.rubble_count)
    
            
    def on_loop(self):
        self.player.update()
        self.rubble.update()
        
        for item in self.all_items:
            self.screen.blit(item.image, item.rect)

        #this is where the collision detection should go
        if pygame.sprite.spritecollide(self.player, self.rubble, False):
            print("collision detected")
            self.player.rect.center  = (self.width / 2, self.height / 2)
            
                
    def on_render(self):
        # Clear the screen by filling it with the background
        self.screen.blit(self.background, (0, 0))
        self.all_items.draw(self.screen)
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