#The MIT License (MIT)

#Copyright (c) 2012 Robin Duda, (chilimannen)

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

#Camera module will keep track of sprite offset.

import os, sys, pygame, random, array
import maps
from pygame.locals import *

#Import game modules.
from loader import load_image
import player, camera


MAP_WIDTH = 1800
MAP_HEIGHT = 1000



#Main function.
def main():
#initialize objects.
    clock = pygame.time.Clock()
    running = True
    car = player.Player()
    cam = camera.Camera()



#create sprite groups.
    map_s     = pygame.sprite.Group()
    player_s  = pygame.sprite.Group()

    tracks_s  = pygame.sprite.Group()
    target_s  = pygame.sprite.Group()

    timer_alert_s = pygame.sprite.Group()
    bound_alert_s = pygame.sprite.Group()
    menu_alert_s = pygame.sprite.Group()

#generate tiles
    map_s.add(maps.Map(MAP_WIDTH/2, MAP_HEIGHT/2))
    player_s.add(car)


    while running:


        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if (keys[K_q]):
                    pygame.quit()
                    sys.exit(0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                    break

#Check for key input. (KEYDOWN, trigger often)
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            car.steerleft()
        if keys[K_RIGHT]:
            car.steerright()
        if keys[K_UP]:
            car.speed = 10
        else:
            car.speed = 0
        if keys[K_DOWN]:
            car.speed = -10

        cam.set_pos(car.x, car.y)

#Show text data.
        text_fps = font.render('FPS: ' + str(int(clock.get_fps())), 1, (224, 16, 16))
        textpos_fps = text_fps.get_rect(centery=25, centerx=60)

#Render Scene.
        screen.blit(background, (0,0))

        #cam.set_pos(car.x, car.y)
        #map = maps.Map(cam.x, cam.y)
        #map.update(cam.x, cam.y)
        #map_s.add(map)
        #map_s.draw(screen)

#Just render..
        tracks_s.update(cam.x, cam.y)
        tracks_s.draw(screen)

        map_s.update(cam.x, cam.y)
        map_s.draw(screen)
        
        player_s.update(cam.x, cam.y)
        player_s.draw(screen)

        target_s.update(cam.x, cam.y)
        target_s.draw(screen)

            
#Blit Blit..       
        screen.blit(text_fps, textpos_fps)
        pygame.display.flip()

#Check collision!!!

        clock.tick(64)
        

#initialization
pygame.init()

screen = pygame.display.set_mode((1500, 800))


pygame.display.set_caption('RoboSimAI')
pygame.mouse.set_visible(False)
font = pygame.font.Font(None, 24)

CENTER_W =  int(pygame.display.Info().current_w /2)
CENTER_H =  int(pygame.display.Info().current_h /2)

#new background surface
background = pygame.Surface(screen.get_size())
background = background.convert_alpha()
background.fill((190, 190, 190))

#Enter the mainloop.
main()

pygame.quit()
sys.exit(0)













        

