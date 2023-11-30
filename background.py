from game_parameters import *
def draw_background(screen):
    #load images
    setting=pygame.image.load("sprites_final/kenney_background-elements-redux/Backgrounds/backgroundColorDesert.png").convert()
    laxis = pygame.image.load("sprites_final/axis.png").convert()
    raxis = pygame.image.load("sprites_final/axis.png").convert()
    raxis = pygame.transform.flip(raxis, True, False)
    #make pngs transparent
    laxis.set_colorkey((255,255,255))
    raxis.set_colorkey((255, 255, 255))
    #fill the screen with background
    screen.blit(setting, (0,0))
    #fill in axis
    screen.blit(laxis, (85, screen_height - tile_size - 120))
    screen.blit(raxis, (620, screen_height - tile_size - 110))

