from vector import Vec2d
from quadtree import Point, AABB, Circle

def contains(shape, point:Point):
	if type(shape) is AABB   : return aabb_contains_point(shape, point)
	if type(shape) is Circle : return circle_contains_point(shape, point)

def intersects(aabb:AABB, shape):
	if type(shape) is AABB   : return aabb_intersects_aabb(aabb, shape)
	if type(shape) is Circle : return circle_intersects_aabb(shape, aabb)


def aabb_contains_point(aabb:AABB, point:Point):
	return point.pos.x > aabb.pos.x and point.pos.x < aabb.pos.x + aabb.size.w\
		and point.pos.y > aabb.pos.y and point.pos.y < aabb.pos.y + aabb.size.h

def circle_contains_point(circle:Circle, point:Point):
	return circle.pos.dist(point.pos) <= circle.radius**2


def aabb_intersects_aabb(a:AABB, b:AABB):
	return (abs((a.pos.x + a.size.w/2) - (b.pos.x + b.size.w/2)) * 2 < (a.size.w + b.size.w)) and\
			(abs((a.pos.y + a.size.h/2) - (b.pos.y + b.size.h/2)) * 2 < (a.size.h + b.size.h))

def circle_intersects_aabb(circle:Circle, aabb:AABB):
	outer_rad = aabb.center.sub(aabb.pos).length
	inner_rad = Vec2d(aabb.center.x, aabb.pos.y).sub(aabb.center).length
	closest_point = aabb.center.sub(circle.pos).normalised().mult(circle.radius).add(circle.pos)

	if circle.pos.dist(aabb.center) >  (circle.radius + outer_rad)**2 : return False
	if circle.pos.dist(aabb.center) <= (circle.radius + inner_rad)**2 : return True
	return aabb_contains_point(aabb, Point(closest_point))



