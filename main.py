import pygame
import background
import spaceship
from spaceship import*
from space_rubble import*
from ship_explosion import *
from explosion import *
from game_level import *
from pygame.locals import *
from title_screen import TitleScreen
from game_header import *
 
# Basic Starting Class
class App:
    
    def __init__(self):
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 800, 600
        background_image = pygame.image.load("starysky.png")
        self.background = pygame.transform.scale(background_image, self.size)
        self.ship = None
        self.title_screen = TitleScreen()
        self.explosions = pygame.sprite.Group()


    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.player = Spaceship(self.screen, 400, 300, screen_width=770, screen_height=570)
        self.level = game_level()

        # Create asteroid event group and add player 
        self.add_rubble = pygame.USEREVENT + 1
        pygame.time.set_timer(self.add_rubble, 1500)

        self.rubble = pygame.sprite.Group()
        self.all_items = pygame.sprite.Group()
        self.all_items.add(self.player)

        self.rubble_count = 0
        self.max_rubble = self.level.get_max_rubble()

        # initiate lives graphic
        self.lives = game_header(self.screen)

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
        if len(self.rubble) == 0:
            self.level.next_level()
            self.rubble_count = 0
    
            
    def on_loop(self):
        self.player.update()
        self.rubble.update()
        self.explosions.update()

        # Bullet-asteroid collision detection
        for bullet in self.player.bullets[:]:  # Iterate over a copy of the bullet list to safely modify the original

            # Check for collision with each asteroid
            for asteroid in self.rubble.sprites():
                if bullet.rect.colliderect(asteroid.rect):  # Check for collision
                    self.player.bullets.remove(bullet)  # Remove bullet
                    asteroid.hit()

                    # Create and add an explosion at the asteroid's position
                    explosion = Explosion(asteroid.rect.center)
                    self.explosions.add(explosion)

                    self.rubble.remove(asteroid)  # Remove asteroid
                    break  # Stop checking this bullet, as it’s already removed

        self.player.draw()

        # asteroid/player collision detectioon
        if pygame.sprite.spritecollide(self.player, self.rubble, False):
            explosion = Explosion(self.player.rect.center)
            self.explosions.add(explosion)
            self.player.rect.center  = (self.width / 2, self.height / 2)
            self.lives.remove_life()
            if self.lives.get_lives() == 0:
                self._running = False          


    def on_render(self):
        # Clear the screen by filling it with the background
        self.screen.blit(self.background, (0, 0))
        self.lives.draw()
        self.player.draw()
        self.all_items.draw(self.screen)
        self.explosions.draw(self.screen)
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()
 

    # The excute block which runs the loop reners an cleanup
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        self.title_screen.show(self.screen)
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
