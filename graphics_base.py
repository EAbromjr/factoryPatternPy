import pygame

window_dimensions = (600, 600)
pygame.init()
screen = pygame.display.set_mode(window_dimensions)

x = 100
y = 100
rect_width = 20
rect_height = 20

player_quits = False

while not player_quits:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			player_quits = True
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_UP]: y -= 4
		if pressed[pygame.K_DOWN]: y += 4
		if pressed[pygame.K_LEFT]: x -= 4
		if pressed[pygame.K_RIGHT]: x += 4
		screen.fill((0, 0, 0))
		if pygame.Rect.x < 0:
			x = 0
		if pygame.Rect.y < 0:
			y = 0
		if pygame.Rect.x + rect_width > window_dimensions[0]:
			x = window_dimensions[0] - rect_width
		if pygame.Rect.y + rect_height > window_dimensions[1]:
			y = window_dimensions[1] - rect_height
		pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, y, 20, 10))

	pygame.display.update()
	pygame.display.flip()
