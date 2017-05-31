class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Point(x=%d, y=%d)" % (self.x, self.y))

class Point2D:

    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def show(self):
        print("Point2D(x2=%d, y2=%d)" % (self.x2, self.y2))

# class Point3D(Point2D, Point):  # Does't works as MRO is changed for __init__(n1, n2)
class Point3D(Point, Point2D):

    def __init__(self, x, y, z):
        self.z = z

        # Python3 syntax only, super() with no arg
        # super() would call parent's first matching method based on mro
        # in this case Point's __init__() with 2 args
        super().__init__(x, y)

        # Python2 compatible syntax
        # super(Point3D, self).__init__(x, y)

        # for other class 'required' __init__(), called it manually like below
        Point2D.__init__(self, x, y)

    def show(self):
        print("Point3D(x=%d, y=%d, z=%d)" % (self.x, self.y, self.z))
        print("-Point2D(x2=%d, y2=%d)" % (self.x2, self.y2))


p1 = Point(1,2)
p2 = Point3D(11,21,31)
p1.show()
p2.show()

# MRO - Method Resolution Order
print(Point3D.__mro__)

