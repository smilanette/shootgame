
from game_parameters import *

class Cannonright(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        # super().__init__()
        self.image = pygame.image.load("sprites_final/cannon.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image=pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def drawcannonright(self, screen):
        screen.blit(self.image, self.rect)