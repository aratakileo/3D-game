from config import*
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = pdata.pos
        self.angle = pdata.angle
        self.sensitivy = 0.004

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        self.keyboard()
        self.mouse()
        self.angle %= double_pi

    def mouse(self):
        if pygame.mouse.get_focused():
            diff = pygame.mouse.get_pos()[0] - hWIDTH
            pygame.mouse.set_pos((hWIDTH, hHEIGHT))
            self.angle += diff * self.sensitivy

    def keyboard(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += pdata.speed * cos_a
            self.y += pdata.speed * sin_a
        elif keys[pygame.K_s]:
            self.x += -pdata.speed * cos_a
            self.y += -pdata.speed * sin_a
        elif keys[pygame.K_a]:
            self.x += pdata.speed * sin_a
            self.y += -pdata.speed * cos_a
        elif keys[pygame.K_d]:
            self.x += -pdata.speed * sin_a
            self.y += pdata.speed * cos_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02