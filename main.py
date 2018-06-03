import pygame

BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
screen.fill(BLACK)
pygame.display.set_caption("GeekSchool Platformer")
clock = pygame.time.Clock()

running = True
while running:
	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
	
	pygame.display.flip()

pygame.quit()
