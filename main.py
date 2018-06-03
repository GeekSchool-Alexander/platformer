import pygame

BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 600
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("GeekSchool Platformer")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

running = True
while running:
	clock.tick(FPS)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
	
	all_sprites.update()
	
	screen.fill(BLACK)
	all_sprites.draw(screen)
	pygame.display.flip()

pygame.quit()
