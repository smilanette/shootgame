
from game_parameters import *

class OOF(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        # super().__init__()
        self.image = pygame.image.load("sprites_final/oof.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def drawoof(self, screen):
        screen.blit(self.image, self.rect)