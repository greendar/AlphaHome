from vectors import *

a = Vector(3,4,5)
b = Vector(1,2,3)
c = Vector(5,6,7)

line = Line(b, c)
print(line)
plane = Plane(a, b, c)
print(plane)
