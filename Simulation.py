import os, sys, pygame, random, array
import maps
from pygame.locals import *

from loader import load_image
import player
import camera
import roborange


MAP_WIDTH = 1800
MAP_HEIGHT = 1000


class Simulation:
    def main(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if (keys[K_q]):
                        pygame.quit()
                        sys.exit(0)

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.running = False
                        break
            self.check_collision(self.car, self.map_s)

            keys = pygame.key.get_pressed()

            if keys[K_LEFT]:
                self.car.steerleft()
                self.robrange.steerleft()
                self.car.animation(self.animation_count)
                if self.animation_count > 14:
                    self.animation_count = 0
                self.animation_count += 1

            if keys[K_RIGHT]:
                self.car.steerright()
                self.robrange.steerright()
                self.car.animation(self.animation_count)
                if self.animation_count > 14:
                    self.animation_count = 0
                self.animation_count += 1

            if keys[K_UP]:
                self.car.animation(self.animation_count)
                if self.animation_count > 14:
                    self.animation_count = 0
                self.animation_count += 1
                self.car.speed = 10
            else:
                self.car.speed = 0

            if keys[K_DOWN]:
                self.car.animation(self.animation_count)
                if self.animation_count > 14:
                    self.animation_count = 0

                self.animation_count += 1
                self.car.speed = -10

            self.cam.set_pos(self.car.x, self.car.y)

    #Show text data.
            text_fps = self.font.render('FPS: ' + str(int(self.clock.get_fps())), 1, (224, 16, 16))
            textpos_fps = text_fps.get_rect(centery=25, centerx=60)

            self.screen.blit(self.background, (0, 0))



    #Just render..
            #self.tracks_s.update(self.cam.x, self.cam.y)
            #self.tracks_s.draw(self.screen)

            self.map_s.update(self.cam.x, self.cam.y)
            self.map_s.draw(self.screen)


            self.player_s.update(self.cam.x, self.cam.y)
            self.player_s.draw(self.screen)

            self.range_s.update(self.cam.x, self.cam.y)
            self.range_s.draw(self.screen)
            #self.target_s.update(self.cam.x, self.cam.y)
            #self.target_s.draw(self.screen)

            self.screen.blit(text_fps, textpos_fps)

            pygame.display.update()
            self.clock.tick(64)

    #initialization
    def check_collision(self, sprite, sprite_group):
        if pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask):
            self.car.reset()
            self.robrange.reset()

    def __init__(self):

        pygame.init()
        self.map_s = pygame.sprite.Group()
        self.player_s = pygame.sprite.Group()
        self.tracks_s = pygame.sprite.Group()
        self.target_s = pygame.sprite.Group()
        self.range_s = pygame.sprite.Group()
        self.animation_count = 0
        self.timer_alert_s = pygame.sprite.Group()
        self.bound_alert_s = pygame.sprite.Group()
        self.menu_alert_s = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((1500, 800))
        self.clock = pygame.time.Clock()
        self.running = True
        self.car = player.Player()
        self.cam = camera.Camera()
        self.robrange = roborange.RoRange()
        self.current_map = maps.Map(500, 1000)

        self.map_s.add(self.current_map)
        self.player_s.add(self.car)
        self.range_s.add(self.robrange)
        pygame.display.set_caption('RoboSimAI')
        pygame.mouse.set_visible(True)
        self.font = pygame.font.Font(None, 24)

        self.background = pygame.Surface(self.screen.get_size())

        self.background.fill((210, 210, 250))



if __name__ == "__main__":
    sim = Simulation()
    sim.main()
    pygame.quit()
    sys.exit(0)
















        

