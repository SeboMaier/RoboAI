import pygame
import os
import math
# from time import sleep
# import numpy
# import neat
pygame.init()


WIN_WIDTH = 1800
WIN_HEIGHT = 1000

BG_IMG = pygame.image.load(os.path.join("imgs", "bg.png"))
ROBO_IMG = pygame.image.load(os.path.join("imgs", "robo.png"))


class Robot:
    ANG_VEL = 100
    FWD_VEL = 10
    IMG = ROBO_IMG

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.yaw = 0

    def move(self, direction):

        # displacement
        dx = -math.sin(self.yaw) * direction * self.FWD_VEL
        dy = -math.cos(self.yaw) * direction * self.FWD_VEL

        self.x = self.x + dx
        self.y = self.y + dy

    def turn(self, direction):
        if direction == "CW":
            self.yaw -= self.ANG_VEL*2*math.pi/360
        if direction == "CCW":
            self.yaw -= -self.ANG_VEL*2*math.pi/360

    def draw(self, win):
        orig_rect = self.IMG.get_rect()
        rot_image = pygame.transform.rotate(self.IMG, self.yaw)
        rot_rect = rot_image.get_rect(center=orig_rect.center)
        # rotated_image = pygame.transform.rotate(self.IMG, self.yaw)
        # new_rect = rotated_image.get_rect(center=self.IMG.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rot_image, rot_rect.topleft)


def draw_window(win, robot):
    win.blit(BG_IMG, (0, 0))
    robot.draw(win)
    pygame.display.update()


def main():
    run = True
    robo = Robot(900, 500)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("RoboSimulation")
    clock = pygame.time.Clock()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            robo.move(1)

        if keys[pygame.K_DOWN]:
            robo.move(-1)

        if keys[pygame.K_LEFT]:
            robo.turn("CCW")

        if keys[pygame.K_RIGHT]:
            robo.turn("CW")

        draw_window(win, robo)
        clock.tick(30)


main()
