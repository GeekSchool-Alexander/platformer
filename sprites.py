import pygame as pg

from VectorClass import Vec2d
from settings import *


class Player(pg.sprite.Sprite):
	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		# animation
		self.frames = (pg.image.load("./images/ball.png"),
		            pg.image.load("./images/ball2.png"),
		            pg.image.load("./images/ball3.png"),
		            pg.image.load("./images/ball4.png"),
		            pg.image.load("./images/ball5.png"),
		            pg.image.load("./images/ball6.png"),
		            pg.image.load("./images/ball7.png"),
		            pg.image.load("./images/ball8.png"))
		self.current_frame = 0
		self.image = self.frames[self.current_frame]
		self.last_update = pg.time.get_ticks()
		
		
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.pos = Vec2d(WIDTH / 2, HEIGHT / 2)
		self.vel = Vec2d(0.0, 0.0)
		self.acc = Vec2d(0.0, 0.0)
		self.game = game
		self.on_the_ground = False
	
	def update(self):
		self.animate()
		self.acc.x = 0
		self.acc.y = PLAYER_GRAVITY
		
		self.moving = ""
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC
			self.moving = "left"
		if keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC
			self.moving = "right"
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
	
	@property
	def height(self):
		return PLAYER_HEIGHT
	
	@property
	def width(self):
		return PLAYER_WIDTH
	
	def jump(self):
		if self.on_the_ground:
			self.vel.y = -5
	
	def animate(self):
		now = pg.time.get_ticks()
		if self.on_the_ground and self.moving:
			if now - self.last_update > 100:
				self.last_update = now
				if self.moving == "right":
					self.current_frame += 1
				elif self.moving == "left":
					self.current_frame -= 1
				
				if self.current_frame == len(self.frames):
					self.current_frame = 0
				elif self.current_frame == -1:
					self.current_frame = len(self.frames)-1
				
				self.image = self.frames[self.current_frame]


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
	
	@property
	def height(self):
		return PLATFORM_HEIGHT
	
	@property
	def width(self):
		return PLATFORM_WIDTH
