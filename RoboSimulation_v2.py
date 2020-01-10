import pygame
import os
import robot
import math
# from time import sleep
# import numpy
# import neat
pygame.init()

WIN_WIDTH = 1800
WIN_HEIGHT = 1000

BG_IMG = pygame.image.load(os.path.join("imgs", "bg.png"))
ROBO_IMG = pygame.image.load(os.path.join("imgs", "robo.png"))





def draw_window(win, robo):
    win.blit(BG_IMG, (0, 0))
    robo.draw(win)
    pygame.display.update()


def main():
    run = True
    robo = robot.Robot()
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
            robo.accelerate()

        if keys[pygame.K_DOWN]:
            robo.deaccelerate()

        if keys[pygame.K_LEFT]:
            robo.steerleft()

        if keys[pygame.K_RIGHT]:
            robo.steerright()

        draw_window(win, robo)
        clock.tick(30)


main()



# INIT

