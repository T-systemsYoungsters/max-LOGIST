import pygame
class Block(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__() 
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()