from levels import level1
from sprites import *


class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode(WINDOW_SIZE)
		pg.display.set_caption("GeekSchool Platformer")
		self.clock = pg.time.Clock()
		self.running = True
	
	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.platforms = pg.sprite.Group()
		config = self.create_level(level1)
		for plt in config:
			p = Platform(*plt)
			self.platforms.add(p)
			self.all_sprites.add(p)
		self.player = Player(self)
		self.all_sprites.add(self.player)
		self.run()
	
	def run(self):
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
	
	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.running = False
				self.playing = False
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.running = False
					self.playing = False
				
	
	def update(self):
		ball_move_line = Line(vec(self.player.center_x, self.player.bottom), vec(self.player.center_x, self.player.bottom)+self.player.vel)
		for plat in self.platforms:
			if plat.collide_point(ball_move_line):
				self.player.pos.y = plat.top
				self.player.vel.y = 0
		
		self.all_sprites.update()
	
	def draw(self):
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		pg.display.flip()
	
	def show_start_screen(self):
		pass
	
	def show_go_screen(self):
		pass
	
	def create_level(self, lvl):
		x = y = 0
		config = []
		for row in lvl:  # вся строка
			for col in row:  # каждый символ
				if col == "-":
					config.append((x, y))
				x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
			y += PLATFORM_HEIGHT  # то же самое и с высотой
			x = 0
		return tuple(config)


g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_go_screen()

pg.quit()
