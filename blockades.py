

import pygame
import random
from game_parameters import *


class Blockades(pygame.sprite.Sprite):
    def __init__ (self,x, y):
        super().__init__()
        self.image = pygame.image.load("sprites_final/kenney_rolling-ball-assets/PNG/Default/block_square.png").convert()
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.center = (x,y)
    def draw(self, screen):
        screen.blit(self.image, self.rect)

blockades=pygame.sprite.Group()
