# Quad-Tree
Quad Tree Partitioning system written in and for Python

- [x] Supports AABB and Circle querying

## Usage
```python

from quadtree import AABB, Tree, Point, Circle

# define position and size of the tree
tree = Tree(Vec2d.zero(), size)
# define position and radius
shape = Circle(mouse_pos, 10)

# create and insert a point into the tree
p = Point(mouse_pos)
tree.insert(p)

# returns points inside the shape
points = tree.query(shape)

```

