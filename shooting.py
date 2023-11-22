# creata a pygame sprite class for a fish
import math

import pygame
import random
from game_parameters import *

class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y, percent, angle):
        #super().__init__()
        self.image = pygame.image.load("sprites_final/kenney_rolling-ball-assets/PNG/Default/ball_red_small.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.percent=percent
        self.angle=angle
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def update(self):
        #TODO need to check if player fish went off the screen
        self.x_speed = self.percent * math.cos(self.angle)
        self.y_speed = abs(self.percent * math.sin(self.angle))*-1
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x=self.x
        self.rect.y=self.y



    def draw(self, screen):
        screen.blit(self.image, self.rect)