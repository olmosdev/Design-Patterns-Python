from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1] )
x, y = p
print(x, y)
print(p.x + p.y)
print(p)
print()

t = [15, 16]
print(Point._make(t))
p = Point(x=15, y=16)
print(p._asdict())
print()

p = Point(x=30, y=31)
print(p)
pp = p._replace(x=33)
print(pp)
print()

print(p._fields)
print(getattr(p, 'x'))
print()

Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
print(Pixel(11, 22, 128, 255, 0))
print()

Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
print(Account._field_defaults)
print(Account('premium'))
print()

# To convert a dictionary to a named tuple, use the double-star-operator
d = {'x': 11, 'y': 22}
print(Point(**d))
print()

class Pointt(namedtuple('Pointt', ['x', 'y'])):
    __slots__ = () # This indicates that no new attributes will be allowed on objects of this class.It is used to save memory and make objects a little faster, as it avoids the use of the internal dictionary __dict__.
    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

for p in Pointt(3, 4), Pointt(14, 5/7):
    print(p)
print()

# Subclassing is not useful for adding new, stored fields. Instead, simply create a new named tuple type from the _fields attribute
Point3D = namedtuple('Point3D', Point._fields + ('z',))

# Using Docstrings
Book = namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book in active collection'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title of first printing'
Book.authors.__doc__ = 'List of authors sorted by last name'

