from collections import namedtuple

point = namedtuple('p','a b c')
newPoint = point(23, 45, 67)
print(newPoint)

print(newPoint._fields)
print(newPoint._field_defaults)
newPoint = newPoint._replace(a=55)
print(newPoint)

p2 = point._make('ack')
print(p2)