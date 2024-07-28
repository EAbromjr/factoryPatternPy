import pygame
import random
import sys


class Shape(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def draw(self):
		raise NotImplementedError

	def move(self, direction):
		if direction == 'up':
			self.y -= 4
		elif direction == 'down':
			self.y += 4
		elif direction == 'left':
			self.x -= 4
		elif direction == 'right':
			self.x += 4

	@staticmethod
	def factory(type):
		if type == "Circle":
			return Circle(100, 100)
		if type == "Square":
			return Square(100, 100)
		if type == "Triangle":
			return Triangle(100, 100)
		if type == "Image":
			return Image(100, 100)
		assert 0, "Bad shape requested: " + type


class Image(Shape):
	def draw(self):
		image_path = sys.path[0] + "/Star-Wars-avatar-icon-Darth-Vader-300x300.png"
		image = pygame.image.load_extended(image_path).convert_alpha()
		screen.blit(image, (self.x, self.y))


class Square(Shape):
	def draw(self):
		pygame.draw.rect(screen, (255, 175, 10), pygame.Rect(self.x, self.y, 20, 20))


class Circle(Shape):
	def draw(self):
		pygame.draw.circle(screen, (0, 255, 255), (self.x, self.y,), 10)


class Triangle(Shape):
	def draw(self):
		pygame.draw.polygon(screen, (255, 255, 0), ((self.x, self.y), (self.x + 20, self.y + 20), (self.x + 40, self.y)))


if __name__ == '__main__':
	pygame.init()
	window_dimensions = (600, 600)
	screen = pygame.display.set_mode(window_dimensions)
	pygame.display.set_caption("Shape Game")

	obj = Shape.factory("Image")
	player_quits = False

	while not player_quits:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				player_quits = True

			pressed = pygame.key.get_pressed()
			image = Shape.factory("Image")
			circle = Shape.factory("Circle")
			square = Shape.factory("Square")
			triangle = Shape.factory("Triangle")
			shapes_list = [circle, square, triangle]
			# for shape in shapes_list:
			if pressed[pygame.K_y]:
				n = random.randint(0, 2)
				obj = shapes_list[n]

			if obj == square:
				if pressed[pygame.K_c]: obj = circle  # TODO: refactor this
			elif obj == circle:  # TODO: refactor this
				if pressed[pygame.K_s]: obj = square  # TODO: refactor this
			if pressed[pygame.K_c]: obj = circle  # TODO: refactor this
			if pressed[pygame.K_s]: obj = square  # TODO: refactor this
			if pressed[pygame.K_i]: obj = image  # TODO: refactor this
			if pressed[pygame.K_UP]: obj.move('up')
			if pressed[pygame.K_DOWN]: obj.move('down')
			if pressed[pygame.K_LEFT]: obj.move('left')
			if pressed[pygame.K_RIGHT]: obj.move('right')
			screen.fill((0, 0, 0))
			obj.draw()
		pygame.display.flip()
	pygame.quit()
