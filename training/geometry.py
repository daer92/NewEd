from training.point import Point

a = Point(0, 4)
b = Point(5, 10)

print(a.distance(b), b.distance(a))
print(a == b)
print(a == Point(0, 4))