class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __lt__(self, p2):
        if isinstance(p2, Point):
            print("Point(%d, %d) < Point(%d, %d)" % (self.x, self.y, p2.x, p2.y)) 
            if (self.x <= p2.x) and (self.y <= p2.y):
                return True
            else:
                return False
        elif isinstance(p2, Point3D) and (self.x <= p2.x) and (self.y <= p2.y):
            print("Point(%d, %d) < Point3(%d, %d, %d)" % (self.x, self.y, p2.x, p2.y, p2.z)) 
            return True
        elif isinstance(p2, int) and (self.x <= p2):
            print("Point(%d, %d) < Int(%d)" % (self.x, self.y, p2)) 
            return True
        elif isinstance(p2, tuple) and (len(p2) >= 2) and (self.x <= p2[0]) and (self.y <= p2[1]):
            print("Point(%d, %d) < Tuple(%d, %d)" % (self.x, self.y, p2[0], p2[1])) 
            return True

        print("Point '<' defult False ")
        return False

class Point3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __lt__(self, p2):
        if isinstance(p2, Point3D) and (self.x <= p2.x) and (self.y <= p2.y) and (self.z <= p2.z):
            return True
        elif isinstance(p2, Point) and (self.x <= p2.x) and (self.y <= p2.y):
            return True
        elif isinstance(p2, int) and (self.z <= p2):
            return True
        elif isinstance(p2, tuple) and (len(p2) >= 3) and (self.x <= p2[0]) and (self.y <= p2[1]) and (self.z <= p2[2]):
            return True

        return False


p2d_1 = Point(10,21)
p2d_2 = Point(12,22)

p3d_1 = Point3D(10,21,20)
p3d_2 = Point3D(12,22,40)


print(p2d_1 < p2d_2)
print(p2d_2 < p2d_1)


print(p2d_1 < 12)
print(p2d_2 < 10)

print(p2d_1 < (12, 22))


# print(p3d_1 < p3d_2)
# print(p3d_2 < p3d_1)

print(p2d_1 < p3d_1)
print(p3d_1 < p2d_1)