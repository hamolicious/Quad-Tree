import pygame
from time import time

#region pygame init
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_icon(screen)
clock, fps = pygame.time.Clock(), 0

delta_time = 0 ; frame_start_time = 0
#endregion

from vector import Vec2d, Color
from quadtree import AABB, Tree, Point, Circle

tree = Tree(Vec2d.zero(), size)
shapes = [AABB, Circle]
shape_index = 0

klock = mlock = False ; counter = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	frame_start_time = time()
	screen.fill(0)

	mouse_pos   = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed()
	key_press   = pygame.key.get_pressed()

	points = []
	if mouse_press[2]:
		shape = shapes[shape_index](mouse_pos, 100)
		if shape_index == 0 : pygame.draw.rect(screen, [0, 255, 0], (shape.pos.as_ints(), shape.size.as_ints()), 1)
		if shape_index == 1 : pygame.draw.circle(screen, [0, 255, 0], shape.pos.as_ints(), shape.radius, 1)
		points = tree.query(shape)

	if mouse_press[0] and not mlock:
		p = Point(mouse_pos)
		tree.insert(p)
		mlock = True

	if key_press[pygame.K_LEFT] and not klock:
		shape_index += 1
		klock = True
	if key_press[pygame.K_RIGHT] and not klock:
		shape_index -= 1
		klock = True

	if shape_index > len(shapes)-1 : shape_index = 0
	if shape_index < 0             : shape_index = len(shapes)-1

	if key_press[pygame.K_SPACE] and counter % 10 == 0:
		p = Point(Vec2d.random_pos() * size)
		tree.insert(p)
	counter += 1

	if sum(mouse_press) == 0 : mlock = False
	if sum(key_press)   == 0 : klock = False

	tree.draw(screen)

	for p in points:
		pygame.draw.circle(screen, [0, 0, 255], p.pos.as_ints(), 2)

	pygame.display.update()
	clock.tick(fps)
	delta_time = time() - frame_start_time
	pygame.display.set_caption(f'Framerate: {int(clock.get_fps())}')