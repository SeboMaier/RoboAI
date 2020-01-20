import pygame
import os
from loader import load_image
from random import randint


class Holes(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("hole.png", False)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.x = randint(0, 1750)
        self.y = randint(0, 950)

        # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y