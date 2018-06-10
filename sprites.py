import pygame as pg

from VectorClass import Vec2d
from settings import *


class Player(pg.sprite.Sprite):
	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("./images/ball.png")
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.pos = Vec2d(WIDTH / 2, HEIGHT / 2)
		self.vel = Vec2d(0.0, 0.0)
		self.acc = Vec2d(0.0, 0.0)
		self.game = game
	
	def update(self):
		self.acc.x = 0
		self.acc.y = PLAYER_GRAVITY
		
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC
		if keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC
		if keys[pg.K_UP]:
			self.jump()
		
		self.acc.x += self.vel.x * PLAYER_FRICTION
		self.vel += self.acc
		self.pos += self.vel + self.acc / 2
		
		if self.right > WIDTH:
			self.pos.x = WIDTH - PLAYER_WIDTH / 2
		if self.left < 0:
			self.pos.x = 0 + PLAYER_WIDTH / 2
		
		self.rect.midbottom = self.pos
	
	@property
	def top(self):
		return self.rect.top
	
	@property
	def bottom(self):
		return self.rect.bottom
	
	@property
	def left(self):
		return self.rect.left
	
	@property
	def right(self):
		return self.rect.right
	
	@property
	def center_x(self):
		return self.rect.center[0]
	
	@property
	def center_y(self):
		return self.rect.center[1]
	
	def jump(self):
		self.rect.x += 1
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.x -= 1
		if hits:
			self.vel.y = -5

class Platform(pg.sprite.Sprite):
	def __init__(self, x, y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load("./images/platform.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	
	@property
	def top(self):
		return self.rect.top
	
	@property
	def bottom(self):
		return self.rect.bottom
	
	@property
	def left(self):
		return self.rect.left
	
	@property
	def right(self):
		return self.rect.right
	
	@property
	def center_x(self):
		return self.rect.center[0]
	
	@property
	def center_y(self):
		return self.rect.center[1]