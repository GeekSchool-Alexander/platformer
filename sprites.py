import pygame as pg

from VectorClass import Vec2d
from settings import *


class Player(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface(PLAYER_SIZE)
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.pos = Vec2d(WIDTH / 2, HEIGHT / 2)
		self.vel = Vec2d(0.0, 0.0)
		self.acc = Vec2d(0.0, 0.0)
	
	def update(self):
		self.acc.x = 0
		self.acc.y = 0
		
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC
		if keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC
		
		self.acc += self.vel * PLAYER_FRICTION
		self.vel += self.acc
		self.pos += self.vel + self.acc / 2
		
		self.rect.center = self.pos
		
		if self.rect.right > WIDTH:
			self.pos.x = WIDTH - PLAYER_WIDTH / 2
		if self.rect.left < 0:
			self.pos.x = 0 + PLAYER_WIDTH / 2
