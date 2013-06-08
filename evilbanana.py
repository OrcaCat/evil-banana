''' Cat platformer canvas V 0.2 by OrcaCat and GraviPy
    For Evil Banana project '''


# Follow PEP8 people!


import pygame
import sys
#from pygame.locals import *
import random


class BananaEntity(object):

    def __init__(self, x, y, health, xvel, yvel, gPixDat):
        self.x = x
        self.y = y
        self.health = health
        self.xvel = xvel
        self.yvel = yvel
        self.gPixDat = gPixDat

    def renderOnScreen(self, screen):
        screen.blit(self.gPixDat, (self.x, self.y))

    def doTick(self):
        self.xvel *= 0.9
        self.yvel *= 0.9
        self.yvel += 4
        self.x += self.xvel
        self.y += self.yvel
        if self.y > 200:
            self.y = 200
            self.yvel = 0
        if self.x > 270:
            self.x = 270
        if self.x < 0:
            self.x = 0


class Player(BananaEntity):

    def __init__(self, x, y, health, xvel, yvel, gPixDat):
        BananaEntity.__init__(self, x, y, health, xvel, yvel, gPixDat)
        self.arrowsPressed = [False, False, False, False]

    def doTick(self):
        self.xvel *= 0.9
        self.yvel *= 0.9
        self.yvel += 4
        self.x += self.xvel
        self.y += self.yvel
        if self.y > 200:
            self.y = 200
            self.yvel = 0
        if self.x > 270:
            self.x = 270
        if self.x < 0:
            self.x = 0
        if self.arrowsPressed[0]:  # If up arrow is pressed
            if self.y >= 200:
                self.yvel = -40
        if self.arrowsPressed[3]:  # If right arrow is pressed
            self.xvel += 2
        if self.arrowsPressed[2]:  # If left arrow is pressed
            self.xvel -= 2


class Enemy(BananaEntity):

    def __init__(self, x, y, health, xvel, yvel, gPixDat):
        BananaEntity.__init__(self, x, y, health, xvel, yvel, gPixDat)


def newEnemy(x, y, health, xvel, yvel, gPixDat, group):
    group.append(Enemy(x, y, health, xvel, yvel, gPixDat))


pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Platformer Canvas')
playerimg = pygame.image.load('banana.png')
protoBanana = Player(10, 10, 10, 0, 0, playerimg)
badBananas = []
while True:
    DISPLAYSURF.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                protoBanana.arrowsPressed[0] = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                protoBanana.arrowsPressed[3] = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                protoBanana.arrowsPressed[2] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                protoBanana.arrowsPressed[0] = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                protoBanana.arrowsPressed[3] = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                protoBanana.arrowsPressed[2] = False
    protoBanana.doTick()
    protoBanana.renderOnScreen(DISPLAYSURF)
    for i in badBananas:
        i.doTick()
        i.renderOnScreen(DISPLAYSURF)
    pygame.display.update()
    fpsClock.tick(FPS)
pygame.quit()
