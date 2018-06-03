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
		for platform_setting in PLATFORM_LIST:
			p = Platform(*platform_setting)
			self.platforms.add(p)
			self.all_sprites.add(p)
		self.player = Player()
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
		self.all_sprites.update()
		hits = pg.sprite.spritecollide(self.player, self.platforms, False)
		if hits:
			self.player.pos.y = hits[0].rect.top
			self.player.vel.y = 0
		
	def draw(self):
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		pg.display.flip()
	
	def show_start_screen(self):
		pass
	
	def show_go_screen(self):
		pass


g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_go_screen()

pg.quit()
