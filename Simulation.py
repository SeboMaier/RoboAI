import os, sys, pygame, random, array
import maps
from pygame.locals import *

from loader import load_image
import player
import camera
import roborange
import holes


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
            if self.check_collision(self.car, self.map_s):
                self.car.reset()
                self.robrange.reset()

            keys = pygame.key.get_pressed()

            if keys[K_SPACE]:
                spritelist = self.check_collision(self.robrange, self.hole_s, True)
                self.score += len(spritelist)*self.holescore

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
            text_fps = self.font.render('FPS: ' + str(int(self.clock.get_fps())), 1, (255, 127, 0))
            textpos_fps = text_fps.get_rect(centery=25, centerx=60)
            text_score = self.font.render("Score: " + str(self.score), 1, (255, 127, 0))
            textpos_score = text_score.get_rect(centery=50, centerx=60)

            self.screen.blit(self.background, (0, 0))



    #Just render..
            self.path_s.update(self.cam.x, self.cam.y)
            self.path_s.draw(self.screen)

            self.range_s.update(self.cam.x, self.cam.y)
            self.range_s.draw(self.screen)

            self.map_s.update(self.cam.x, self.cam.y)
            self.map_s.draw(self.screen)


            self.player_s.update(self.cam.x, self.cam.y)
            self.player_s.draw(self.screen)


            self.hole_s.update(self.cam.x, self.cam.y)
            self.hole_s.draw(self.screen)

            self.screen.blit(text_fps, textpos_fps)
            self.screen.blit(text_score, textpos_score)

            pygame.display.update()
            self.clock.tick(64)

    #initialization
    def check_collision(self, sprite, sprite_group, dokill=False):
        spritelist = pygame.sprite.spritecollide(sprite, sprite_group, dokill, pygame.sprite.collide_mask)
        if spritelist:
            return spritelist
        else:
            return []

    def __init__(self):

        pygame.init()

        self.score = 0
        self.holescore = 10
        self.map_s = pygame.sprite.Group()
        self.player_s = pygame.sprite.Group()
        self.path_s = pygame.sprite.Group()
        self.hole_s = pygame.sprite.Group()
        self.range_s = pygame.sprite.Group()
        self.animation_count = 0
        self.timer_alert_s = pygame.sprite.Group()
        self.bound_alert_s = pygame.sprite.Group()
        self.menu_alert_s = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((1500, 800))
        for r in range(20):
            self.hole = holes.Holes()
            self.hole.add(self.hole_s)

        self.clock = pygame.time.Clock()
        self.running = True
        self.car = player.Player()
        self.cam = camera.Camera()
        self.robrange = roborange.RoRange()
        self.current_map = maps.Map()


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
















        

