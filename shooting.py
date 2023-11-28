# creata a pygame sprite class for a fish
import math
import time

import pygame
import random
from game_parameters import *

class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y, percent, angle, start):
        #super().__init__()
        self.image = pygame.image.load("sprites_final/kenney_rolling-ball-assets/PNG/Default/ball_red_small.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.percent=percent
        self.angle=angle
        self.start=start
        self.x = x
        self.y = y
        self.rect.center = (x, y)
    def update(self):
        end=time.perf_counter()
        self.x_speed = self.percent * 0.1*math.cos(self.angle)
        self.y_speed = abs(self.percent * 0.6*math.sin(self.angle))*-1 + ((self.percent/(self.percent+1))*(3*(end-self.start)))
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x=self.x
        self.rect.y=self.y



    def draw(self, screen):
        screen.blit(self.image, self.rect)