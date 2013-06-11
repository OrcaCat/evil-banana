''' Cat platformer canvas V 0.2 by OrcaCat, GraviPy, and Falling Duck
    For Evil Banana project '''


import pygame
#import sys
import random


class BananaEntity(pygame.sprite.Sprite):

    def __init__(self, x, y, health, xVel, yVel, gPixDat):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.xVel = xVel
        self.yVel = yVel

        self.image = gPixDat
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def _tick(self):
        self.xVel *= 0.9
        self.yVel *= 0.9
        self.yVel += 4
        self.rect.x += self.xVel
        self.rect.y += self.yVel
        if self.rect.y > 200:
            self.rect.y = 200
            self.yVel = 0
        if self.x > 270:
            self.rect.x = 270
        if self.x < 0:
            self.rect.x = 0


class Player(BananaEntity):

    def __init__(self, x, y, health, xVel, yVel, gPixDat):
        BananaEntity.__init__(self, x, y, health, xVel, yVel, gPixDat)
        self.arrowsPressed = [False] * 4

    def tick(self):
        self._tick()
        if self.arrowsPressed[0]:  # If up arrow is pressed
            if self.y >= 200:
                self.yvel = -40
        if self.arrowsPressed[3]:  # If right arrow is pressed
            self.xvel += 2
        if self.arrowsPressed[2]:  # If left arrow is pressed
            self.xvel -= 2


class Enemy(BananaEntity):

    def __init__(self, x, y, health, xVel, yVel, gPixDat):
        BananaEntity.__init__(self, x, y, health, xVel, yVel, gPixDat)


def newEnemy(x, y, health, xVel, yVel, gPixDat, group):
    group.append(Enemy(x, y, health, xVel, yVel, gPixDat))


pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Platformer Canvas')
playerimg = pygame.image.load('banana.png')
goodBananas = pygame.sprite.Group()
protoBanana = Player(10, 10, 10, 0, 0, playerimg)
goodBananas.add(protoBanana)
badBananas = pygame.sprite.Group()
running = True
while running:
    DISPLAYSURF.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                continue
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                protoBanana.arrowsPressed[0] = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                protoBanana.arrowsPressed[3] = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                protoBanana.arrowsPressed[2] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                protoBanana.arrowsPressed[0] = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                protoBanana.arrowsPressed[3] = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                protoBanana.arrowsPressed[2] = False
    protoBanana.tick()
    goodBananas.draw(DISPLAYSURF)
    for i in badBananas:
        i._tick()
    badBananas.draw(DISPLAYSURF)
    pygame.display.update()
    fpsClock.tick(FPS)
pygame.quit()
