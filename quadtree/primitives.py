from vector import Vec2d


class Point:
	def __init__(self, pos: Vec2d) -> None:
		self.pos = Vec2d(pos)


class AABB:
	def __init__(self, pos: Vec2d, size: Vec2d) -> None:
		self.pos = Vec2d(pos)
		self.size = Vec2d(size)
		self.half_size = self.size.div(2)
		self.center = self.pos.add(self.half_size)


class Circle:
	def __init__(self, pos:Vec2d, radius:float) -> None:
		self.pos = Vec2d(pos)
		self.radius = radius
		self.diameter = radius*2

