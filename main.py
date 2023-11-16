from background import draw_background
import pygame
import sys
from game_parameters import *
import random
screen = pygame.display.set_mode((screen_width,screen_height))
running=True
background =screen.copy()
draw_background(background)
#percent
percent_font=pygame.font.Font('sprites_final/Black_Crayon.ttf', 25)
percent=0
while True:
    if event.type == pygame.KEYDOWN:

while True:
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
