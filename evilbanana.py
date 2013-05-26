'''	Cat platformer canvas V 0.2 by OrcaCat and GraviPy
	For Evil Banana project '''
 
import pygame, sys
from pygame.locals import *
import random

class BananaEntity():
	def __init__(self,x,y,health,xvel,yvel,gPixDat):
		self.x=x
		self.y=y
		self.health=health
		self.xvel=xvel
		self.yvel=yvel
		self.gPixDat=gPixDat
	def renderOnScreen(self):
		global DISPLAYSURF
		DISPLAYSURF.blit(self.gPixDat, (self.x, self.y))
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
	def __init__(self,x,y,health,xvel,yvel,gPixDat):
		self.x=x
		self.y=y
		self.health=health
		self.xvel=xvel
		self.yvel=yvel
		self.gPixDat=gPixDat
		self.arrowsPressed=[False,False,False,False]
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
		if self.arrowsPressed[0]: #if up arrow is pressed
			if self.y >= 200:
				self.yvel = -40
		if self.arrowsPressed[3]: #if right arrow is pressed
			self.xvel += 2
		if self.arrowsPressed[2]: #if left arrow is pressed
			self.xvel -= 2
class Enemy(BananaEntity):
	def __init__(self,x,y,health,xvel,yvel,gPixDat):
		self.x=x
		self.y=y
		self.health=health
		self.xvel=xvel
		self.yvel=yvel
		self.gPixDat=gPixDat
def newEnemy(x,y,health,xvel,yvel,gPixDat):
	global badBananas
	badBananas.append(Enemy(x,y,health,xvel,yvel,gPixDat))
pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Platformer Canvas')
playerimg = pygame.image.load('banana.png')
protoBanana = Player(10,10,10,0,0,playerimg)
badBananas=[]
while True:
	DISPLAYSURF.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_UP or event.key == K_w:
				protoBanana.arrowsPressed[0]=True
			if event.key == K_RIGHT or event.key == K_d:
				protoBanana.arrowsPressed[3]=True
			if event.key == K_LEFT or event.key == K_a:
				protoBanana.arrowsPressed[2]=True
		elif event.type == KEYUP:
			if event.key == K_UP or event.key == K_w:
				protoBanana.arrowsPressed[0]=False
			if event.key == K_RIGHT or event.key == K_d:
				protoBanana.arrowsPressed[3]=False
			if event.key == K_LEFT or event.key == K_a:
				protoBanana.arrowsPressed[2]=False
	protoBanana.doTick()
	protoBanana.renderOnScreen()
	for i in badBananas:
		i.doTick()
		i.renderOnScreen()
	pygame.display.update()
	fpsClock.tick(FPS)