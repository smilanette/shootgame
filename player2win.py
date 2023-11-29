import math
import time

import pygame
import random
from game_parameters import *

class TWOWIN(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        # super().__init__()
        self.image = pygame.image.load("sprites_final/player2win.PNG").convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def drawtwo(self, screen):
        screen.blit(self.image, (self.x,self.y))