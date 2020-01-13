import pygame
import os
from loader import load_image


class Map(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bg.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x, self.y - cam_y