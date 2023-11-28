

import pygame
import random
from game_parameters import *


class Powerup(pygame.sprite.Sprite):
    def __init__ (self,x, y):
        super().__init__()
        self.image = pygame.image.load("sprites_final/kenney_rolling-ball-assets/PNG/Default/star.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.center = (x,y)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

health=pygame.sprite.Group()
