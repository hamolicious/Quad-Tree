
from vector import Vec2d
from quadtree import AABB
from quadtree import Point
from quadtree import intersects, contains
import pygame

class Tree:
	def __init__(self, pos, size) -> None:
		self.node_capacity = 4
		self.boundary = AABB(pos, size)

		self.points = []

		self.top_left = None
		self.top_right = None
		self.bottom_left = None
		self.bottom_right = None

	def __subdivide(self):
		half_size = self.boundary.size.copy().div(2)

		self.top_left =     Tree(Vec2d(self.boundary.pos.x              , self.boundary.pos.y), half_size)
		self.top_right =    Tree(Vec2d(self.boundary.pos.x + half_size.x, self.boundary.pos.y), half_size)
		self.bottom_left =  Tree(Vec2d(self.boundary.pos.x              , self.boundary.pos.y + half_size.y), half_size)
		self.bottom_right = Tree(Vec2d(self.boundary.pos.x + half_size.x, self.boundary.pos.y + half_size.y) , half_size)

		for p in self.points:
			if self.top_left.insert(p) : self.points.remove(p) ; continue
			if self.top_right.insert(p) : self.points.remove(p) ; continue
			if self.bottom_left.insert(p) : self.points.remove(p) ; continue
			if self.bottom_right.insert(p) : self.points.remove(p) ; continue

	def insert(self, point: Point):
		if not contains(self.boundary, point) : return False

		if self.top_left is None and len(self.points) < self.node_capacity:
			self.points.append(point)
			return True

		if self.top_left is None and len(self.points) >= self.node_capacity:
			self.__subdivide()

		if self.top_left.insert(point): return True
		if self.top_right.insert(point): return True
		if self.bottom_left.insert(point): return True
		if self.bottom_right.insert(point): return True

		return False

	def query(self, shape):
		result = []

		if not intersects(self.boundary, shape) : return result

		for p in self.points:
			if contains(shape, p) : result.append(p)

		if self.top_left is None : return result

		result += self.top_left.query(shape)
		result += self.top_right.query(shape)
		result += self.bottom_left.query(shape)
		result += self.bottom_right.query(shape)

		return result

	def draw(self, screen):
		pygame.draw.rect(screen, [255, 255, 255], (self.boundary.pos.as_ints(), self.boundary.size.as_ints()), 1)

		for p in self.points:
			pygame.draw.circle(screen, [255, 0, 0], p.pos.as_ints(), 2)

		if self.top_left is None : return

		self.top_left.draw(screen)
		self.top_right.draw(screen)
		self.bottom_left.draw(screen)
		self.bottom_right.draw(screen)
