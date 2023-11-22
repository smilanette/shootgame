import pygame
import random
from game_parameters import *
def draw_background(screen):
    #load our tiles from the assets folder
    #cannon1 = pygame.image.load("sprites_final/cannon.png").convert()
    #cannon2 = pygame.image.load("sprites_final/cannon.png").convert()
    #cannon2 = pygame.transform.flip(cannon2, True, False)
    setting=pygame.image.load("sprites_final/kenney_background-elements-redux/Backgrounds/backgroundColorDesert.png").convert()
    #tower=pygame.image.load("sprites_final/kenney_background-elements-redux/Backgrounds/towerAlt.png").convert()

    #make pngs transparent
    #cannon1.set_colorkey((255,255,255))
    #cannon2.set_colorkey((255, 255, 255))
    #tower.set_colorkey((0, 0, 0))


    #fill the screen with water
    screen.blit(setting, (0,0))
    #fill in cannon
    #screen.blit(cannon1, (20,screen_height-tile_size-60))
    #screen.blit(cannon2, (700, screen_height - tile_size - 60))
    #screen.blit(tower, (370, 270))


#def add_fish(num_fish):
    #for _ in range(num_fish):
        #fishes.add(Fish(random.randint(screen_height, screen_width * 2), random.randint(80, screen_height - (2 * tile_size))))


#def add_enemies(num_enemies):
    #for _ in range(num_enemies):
        #enemies.add(Enemy(random.randint(screen_height, screen_width * 2), random.randint(80, screen_height - (2 * tile_size))))