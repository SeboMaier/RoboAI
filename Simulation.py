import os, sys, pygame, random, array
import maps
from pygame.locals import *
import math

from loader import load_image
import player
import camera
import roborange
import holes
import path
import sensors

PATH = True
USE_SENSORS = True
SHOW_SENSORS = False

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
            if USE_SENSORS:
                text_s1 = self.font.render('S1: ' + str(int(self.sensor1.delta)), 1, (255, 127, 0))
                textpos_s1 = text_s1.get_rect(centery=75, centerx=60)
                text_s2 = self.font.render('S2: ' + str(int(self.sensor2.delta)), 1, (255, 127, 0))
                textpos_s2 = text_s1.get_rect(centery=100, centerx=60)
                text_s3 = self.font.render('S3: ' + str(int(self.sensor3.delta)), 1, (255, 127, 0))
                textpos_s3 = text_s1.get_rect(centery=125, centerx=60)
                text_s4 = self.font.render('S4: ' + str(int(self.sensor4.delta)), 1, (255, 127, 0))
                textpos_s4 = text_s1.get_rect(centery=150, centerx=60)
                text_s5 = self.font.render('S5: ' + str(int(self.sensor5.delta)), 1, (255, 127, 0))
                textpos_s5 = text_s1.get_rect(centery=175, centerx=60)
                text_s6 = self.font.render('S6: ' + str(int(self.sensor6.delta)), 1, (255, 127, 0))
                textpos_s6 = text_s1.get_rect(centery=200, centerx=60)

            self.screen.blit(self.background, (0, 0))

            self.path_s.update(self.cam.x, self.cam.y)
            self.hole_s.update(self.cam.x, self.cam.y)
            self.range_s.update(self.cam.x, self.cam.y)
            self.map_s.update(self.cam.x, self.cam.y)
            self.player_s.update(self.cam.x, self.cam.y)

            if USE_SENSORS:
                self.sensor_s.update(self.car.dir, self.CENTER_X, self.CENTER_Y)
                self.measure(self.sensor_s)

            if PATH:
                self.path.image.fill((255, 127, 0), Rect(self.car.x, self.car.y, 5, 5))
                self.path_s.draw(self.screen)

            self.range_s.draw(self.screen)
            self.map_s.draw(self.screen)
            if SHOW_SENSORS:
                self.sensor_s.draw(self.screen)
            self.player_s.draw(self.screen)
            self.hole_s.draw(self.screen)


            self.screen.blit(text_fps, textpos_fps)
            self.screen.blit(text_score, textpos_score)
            if USE_SENSORS:
                self.screen.blit(text_s1, textpos_s1)
                self.screen.blit(text_s2, textpos_s2)
                self.screen.blit(text_s3, textpos_s3)
                self.screen.blit(text_s4, textpos_s4)
                self.screen.blit(text_s5, textpos_s5)
                self.screen.blit(text_s6, textpos_s6)

            pygame.display.update()
            self.clock.tick(64)

    def check_collision(self, sprite, sprite_group, dokill=False):
        spritelist = pygame.sprite.spritecollide(sprite, sprite_group, dokill, pygame.sprite.collide_mask)
        if spritelist:
            return spritelist
        else:
            return []

    def measure(self, sensor_s):
        for sensor in sensor_s:
            if sensor.rotangle >= 360:
                sensor.rotangle -= 360
            if sensor.rotangle <= 0:
                dx0 = sensor.rect.bottomleft[0]
                dx1 = sensor.rect.bottomleft[1]
            if 0 < sensor.rotangle <= 90:
                dx0 = sensor.rect.bottomright[0]
                dx1 = sensor.rect.bottomright[1]
            if 90 < sensor.rotangle <= 180:
                dx0 = sensor.rect.topright[0]
                dx1 = sensor.rect.topright[1]
            if 180 < sensor.rotangle <= 270:
                dx0 = sensor.rect.topleft[0]
                dx1 = sensor.rect.topleft[1]
            if 270 < sensor.rotangle < 360:
                dx0 = sensor.rect.bottomleft[0]
                dx1 = sensor.rect.bottomleft[1]

            offset_x = -self.current_map.rect.topleft[0] + sensor.rect.topleft[0]
            offset_y = -self.current_map.rect.topleft[1] + sensor.rect.topleft[1]
            sensor.mask = pygame.mask.from_surface(sensor.image)
            if self.current_map.mask.overlap(sensor.mask, (offset_x, offset_y)) is not None:
                ix, iy = self.current_map.mask.overlap(sensor.mask, (offset_x, offset_y))
                dx = - ix - self.current_map.rect.topleft[0] + dx0
                dy = - iy - self.current_map.rect.topleft[1] + dx1
                sensor.delta = math.sqrt(dx ** 2 + dy ** 2)
                if sensor.delta >= 700:
                    sensor.delta = 700
            else:
                sensor.delta = 700

    def __init__(self):

        pygame.init()

        self.score = 0
        self.holescore = 10
        self.map_s = pygame.sprite.Group()
        self.player_s = pygame.sprite.Group()
        self.path_s = pygame.sprite.Group()
        self.hole_s = pygame.sprite.Group()
        self.range_s = pygame.sprite.Group()
        self.sensor_s = pygame.sprite.Group()
        self.animation_count = 0

        self.screen = pygame.display.set_mode((1800, 1000))
        for r in range(20):
            self.hole = holes.Holes()
            self.hole.add(self.hole_s)

        self.clock = pygame.time.Clock()
        self.CENTER_X = int(pygame.display.Info().current_w / 2)
        self.CENTER_Y = int(pygame.display.Info().current_h / 2)
        self.running = True
        self.car = player.Player()
        self.cam = camera.Camera()
        self.robrange = roborange.RoRange()
        self.current_map = maps.Map()
        self.path = path.Path()

        # Sensoren erstellen
        if USE_SENSORS:
            self.sensor1 = sensors.Sensor(0)
            self.sensor2 = sensors.Sensor(30)
            self.sensor3 = sensors.Sensor(150)
            self.sensor4 = sensors.Sensor(180)
            self.sensor5 = sensors.Sensor(210)
            self.sensor6 = sensors.Sensor(330)
            self.sensor_s.add(self.sensor1)
            self.sensor_s.add(self.sensor2)
            self.sensor_s.add(self.sensor3)
            self.sensor_s.add(self.sensor4)
            self.sensor_s.add(self.sensor5)
            self.sensor_s.add(self.sensor6)

        self.map_s.add(self.current_map)
        self.player_s.add(self.car)
        self.range_s.add(self.robrange)
        self.path_s.add(self.path)


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
















        

