import pygame
from random import random

from spaceship import Spaceship
from explosion import Explosion
from game_level import GameLevel
from pygame.locals import *
from title_screen import TitleScreen
from life_header import LifeHeader
from score_calculator import ScoreCalculator
from powerup import PowerUp
from pause_menu import PauseMenu
 

class App:
    
    def __init__(self):
        pygame.init()
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 800, 600
        background_image = pygame.image.load("starysky.png")
        self.background = pygame.transform.scale(background_image, self.size)
        self.ship = None
        self.title_screen = TitleScreen("Asteroids")
        self.explosions = pygame.sprite.Group()
        self.score = ScoreCalculator()
        self.font = pygame.font.SysFont("georgia", 24)
        self.combo = 0
        self.pause_menu = PauseMenu()

        # create sprite groups for enemy objects and all objects
        self.rubble = pygame.sprite.Group()
        self.all_items = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.rubble_count = 0 # counter to control the amount of asteroids per level


    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.player = Spaceship(self.screen, 400, 300, screen_width=770, screen_height=570)
        self.level = GameLevel()

        # create asteroid event group and add player all objects sprite group
        self.add_rubble = pygame.USEREVENT + 1
        self.all_items.add(self.player)

        # create timer for spawn rate of asteroids
        self.spawn_rate = 1500
        pygame.time.set_timer(self.add_rubble, self.spawn_rate)
       
        # initiate lives graphic
        self.lives = LifeHeader(self.screen)

        self._running = True

        # initialize time variables for level up
        self.pause = False
        self.pause_length = 3500
        self.pause_start_time = 0
   
     
    # Basic Game Loop Functions
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        # asteroid spawning and level control
        elif event.type == self.add_rubble and self.pause == False: # only run this condition if game is not paused
            max_rubble = self.level.get_max_rubble()
            self.new_rubble = self.level.get_new_rubble()
            if self.rubble_count < max_rubble: 
                self.rubble.add(self.new_rubble)
                self.all_items.add(self.new_rubble)
            elif len(self.rubble.sprites()) == 0: # condition that indicates level has been cleared
                self.pause = True
                self.pause_start_time = pygame.time.get_ticks()
                self.rubble_count = 0
                self.spawn_rate //= 1.6
                pygame.time.set_timer(self.add_rubble, int(self.spawn_rate)) 
                
            if self.rubble_count != max_rubble:
                self.rubble_count += 1
                print(self.rubble_count)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.pause_menu.show(self.screen, self.score.get_score(), False):
                    self._running = False 

    
            
    def on_loop(self):
        # Calculate time passed, unpause game after pause_length has expired, and proceed to the next level
        if self.pause:
            if pygame.time.get_ticks() - self.pause_start_time > self.pause_length:
                self.pause = False
                self.level.next_level()
            return

        self.player.update()
        self.rubble.update()
        self.explosions.update()
        

        # Bullet-asteroid collision detection
        for bullet in self.player.bullets[:]:  # Iterate over a copy of the bullet list to safely modify the original

            # Check for collision with each asteroid
            for asteroid in self.rubble.sprites():
                if pygame.sprite.collide_mask(bullet, asteroid):  # Check for collision
                    self.player.bullets.remove(bullet)  # Remove bullet
                    asteroid.hit()
                    
                    #combo track num of asteroids hit in curent life, combos every 10 hits
                    self.combo += 1 
                    if self.combo > 0 and self.combo % 10 == 0:
                        self.score.multiplier += 1
                    self.score.increse_score() #increse score

                    # Create and add an explosion at the asteroid's position
                    explosion = Explosion(asteroid.rect.center)
                    self.explosions.add(explosion)

                    self.rubble.remove(asteroid)  # Remove asteroid
                    if random() < 0.1:
                        powerup = PowerUp(asteroid.rect.center)
                        self.powerups.add(powerup)
                        self.all_items.add(powerup)
                    break  # Stop checking this bullet, as it’s already removed

        for powerup in self.powerups.sprites():
            if pygame.sprite.collide_mask(self.player, powerup):
                self.powerups.remove(powerup)
                self.all_items.remove(powerup)
                self.player.ship_level += 1
                self.player.level_up_ship()

        self.player.draw()

        # asteroid/player collision detectioon
        if pygame.sprite.spritecollide(self.player, self.rubble, False, pygame.sprite.collide_mask):
            explosion = Explosion(self.player.rect.center)
            self.explosions.add(explosion)
            self.player.rect.center  = (self.width / 2, self.height / 2)
            self.lives.remove_life()
            #reset the multiplier
            self.score.reset_multiplier()
            self.combo = 0  
            if self.lives.get_lives() == 0:
                self._running = False   


    def on_render(self):
        # Clear the screen by filling it with the background
        self.screen.blit(self.background, (0, 0))
        self.lives.draw()
        self.player.draw()
        self.all_items.draw(self.screen)
        self.explosions.draw(self.screen)

        # Display level cleared text
        if self.pause:
            level_cleared_text, level_cleared_rect = self.level.display_text()
            self.screen.blit(level_cleared_text, level_cleared_rect)
        
        # Displays the score and multiplier
        self.score_txt = "Score: " + str(self.score.get_score())
        self.mult_txt = "Multiplier: " + str(self.score.get_multiplier())
        score_text = self.font.render(self.score_txt + " " + self.mult_txt, True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(10, 10))
        
        self.screen.blit(score_text, score_rect)
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()
 

    # The execute block which runs the loop renders on cleanup
    def on_execute(self, test=False):
        one_run = False
        if self.on_init() == False:
            self._running = False

        self.title_screen.show(self.screen)
 
        while self._running and one_run != True:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            if test:
                one_run = True

        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
