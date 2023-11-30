import pygame

class Start(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        # super().__init__()
        self.image = pygame.image.load("sprites_final/start.png").convert()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))