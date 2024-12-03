import unittest
from main import *
from spaceship import*
from explosion import *
from game_level import *
from pygame.locals import *
from title_screen import *
from life_header import *
from score_calculator import *
from powerup import *
from pause_menu import *
import pygame
from pygame.locals import *
from space_rubble import *


class TestPauseMenu(unittest.TestCase):
    def test_init(self):
        pause_menu = PauseMenu()
        self.assertIsNotNone(pause_menu)
    
    def test_show_exit(self):
        pause_menu = PauseMenu()
        screen = pygame.display.set_mode((800, 600))
        score = 100
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(400, 425))
        pygame.event.post(event)
        self.assertTrue(pause_menu.show(screen, score, True))

    def test_show_resume(self):
        pause_menu = PauseMenu()
        screen = pygame.display.set_mode((800, 600))
        score = 100
        event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(400, 325))
        pygame.event.post(event)
        self.assertFalse(pause_menu.show(screen, score, True))

class TestScore(unittest.TestCase):
    def test_init(self):
        scorekeeper = Score_Calculator()
        self.assertIsNotNone(scorekeeper)

    def test_increse_score(self):
        scorekeeper = Score_Calculator()
        scorekeeper.increse_score()
        self.assertEqual(scorekeeper.score, 10)


    def test_get_score(self):
        scorekeeper = Score_Calculator()
        scorekeeper.increse_score()
        self.assertEqual(scorekeeper.get_score(), 10)

    def test_get_multiplier(self):
        scorekeeper = Score_Calculator()
        self.assertEqual(scorekeeper.get_multiplier(), 1)  
    
    def test_increase_multiplier(self):        
        scorekeeper = Score_Calculator()
        scorekeeper.increase_multiplier()
        self.assertEqual(scorekeeper.get_multiplier(), 2)
        
    def test_reset_multiplier(self):
        scorekeeper = Score_Calculator()
        scorekeeper.increase_multiplier()
        scorekeeper.reset_multiplier()
        self.assertEqual(scorekeeper.get_multiplier(), 1)
        
    def test_multiplier_score(self):
        scorekeeper = Score_Calculator()
        scorekeeper.increse_score()
        scorekeeper.increase_multiplier()
        scorekeeper.increse_score()
        self.assertEqual(scorekeeper.get_score(), 30)
        
class TestMain(unittest.TestCase):
    def test_on_init(self):
        app = App()
        app.on_init()
        self.assertIsNotNone(app.screen)
        self.assertIsNotNone(app.player)
        self.assertIsNotNone(app.level)
        
class TestTitleScreen(unittest.TestCase):

    def test_init(self):
        title_screen = TitleScreen("Test Title")
        self.assertIsNotNone(title_screen.font)
        self.assertIsNotNone(title_screen.button_font)
        self.assertIsNotNone(title_screen.button_rect)
        self.assertEqual(title_screen.text, "Test Title")

    
        
    
    
    
if __name__ == '__main__':
    unittest.main()