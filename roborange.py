import pygame
import math
from loader import load_image


def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


class RoRange(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('range.png', False)
        self.image_orig = self.image
        #self.image.fill((255, 255, 255, 64), None, pygame.BLEND_RGBA_MULT)
        self.rect = self.image.get_rect()
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.CENTER_X = int(pygame.display.Info().current_w / 2)
        self.CENTER_Y = int(pygame.display.Info().current_h / 2)
        self.x = self.CENTER_X
        self.y = self.CENTER_Y

        self.rect.topleft = (self.x - 100, self.y - 200)
        self.mask = pygame.mask.from_surface(self.image)


        self.dir = 0
        self.speed = 0.0
        self.maxspeed = 11.5
        self.minspeed = -1.85
        self.acceleration = 1
        self.deacceleration = 1
        self.softening = 2
        self.steering = 3
        self.tracks = True

    def reset(self):
        self.speed = 0.0
        self.dir = 0
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)
        self.x = self.CENTER_X
        self.y = self.CENTER_Y
        self.rect.topleft = self.x - 100, self.y - 200
        self.mask = pygame.mask.from_surface(self.image)

    def accelerate(self):
        if self.speed < self.maxspeed:
            self.speed = self.speed + self.acceleration

        self.mask = pygame.mask.from_surface(self.image)

    def deaccelerate(self):
        if self.speed > self.minspeed:
            self.speed = self.speed - self.deacceleration

        self.mask = pygame.mask.from_surface(self.image)

    def steerleft(self):
        self.dir = self.dir+self.steering
        if self.dir > 360:
            self.dir = 0
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)
        self.mask = pygame.mask.from_surface(self.image)

    def steerright(self):
        self.dir = self.dir-self.steering
        if self.dir < 0:
            self.dir = 360
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, last_x, last_y):
        self.x = self.x + self.speed * math.cos(math.radians(270-self.dir))
        self.y = self.y + self.speed * math.sin(math.radians(270-self.dir))



