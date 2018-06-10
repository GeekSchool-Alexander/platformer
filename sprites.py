import pygame as pg

from VectorClass import Vec2d as vec
from lines import Line
from settings import *


class GameObject(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = None
		self.rect = None

class Player(GameObject):
	def __init__(self, game):
		super().__init__()
		self.image = pg.image.load("./images/ball.png")
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.pos = vec(WIDTH / 2, HEIGHT / 2)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)
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
	
	@property
	def center(self):
		return vec(self.center_x, self.center_y)
	
	@property
	def side_top(self):
		return Line(vec(self.left, self.top), vec(self.right, self.top))
	
	@property
	def side_bottom(self):
		return Line(vec(self.left, self.bottom), vec(self.right, self.bottom))
	
	@property
	def side_left(self):
		return Line(vec(self.left, self.top), vec(self.left, self.bottom))
	
	@property
	def side_right(self):
		return Line(vec(self.right, self.top), vec(self.right, self.bottom))
	
	def jump(self):
		self.rect.x += 1
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.x -= 1
		if hits and self.vel.y == 0:
			self.vel.y = -5
		

class Platform(pg.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pg.image.load("./images/platform.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	
	def collide_point(self, move_line):
		if isinstance(move_line, Line):
			intersection_points = []
			def get_nearest_point(start_point, points):
				if isinstance(points, list) and isinstance(start_point, vec):
					if points:
						current_nearest_point = points[0]
						distance_to_current_nearest_point = vec(current_nearest_point - start_point).length
						for point in points:
							distance_to_point = vec(point - start_point).length
							if distance_to_point < distance_to_current_nearest_point:
								current_nearest_point = point
						return current_nearest_point
				else:
					raise TypeError
					
			for side in self.sides:
				intersection_point = move_line.intersection(side, True)
				if intersection_point:
					intersection_points.append(intersection_point)
			
			if intersection_points:
				return get_nearest_point(move_line.p1, intersection_points)
		else:
			raise TypeError
			
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
	def center(self):
		return vec(self.center_x, self.center_y)
	
	@property
	def side_top(self):
		return Line(vec(self.left, self.top), vec(self.right, self.top))
	
	@property
	def side_bottom(self):
		return Line(vec(self.left, self.bottom), vec(self.right, self.bottom))
	
	@property
	def side_left(self):
		return Line(vec(self.left, self.top), vec(self.left, self.bottom))

	@property
	def side_right(self):
		return Line(vec(self.right, self.top), vec(self.right, self.bottom))
	
	@property
	def sides(self):
		return tuple((self.side_right, self.side_top, self.side_left, self.side_bottom))
