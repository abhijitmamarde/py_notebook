
class Point:
    '''Defines simple 2D Points'''
    def __init__(self):
        self.x = 10
        self.y = 20
    def __str__(self):
        return "Point(x=%d, y=%d)" % (self.x, self.y)
    def __repr__(self):
        return "P(x=%d, y=%d)" % (self.x, self.y)
    def show(self, flag, capital):
        '''prints the object on command line'''
        print(self.x, self.y)

p = Point()
p.show()

p = Point()
print(p)
print("Point p is:", p)
print("Point p is: %s" % p)
print("Point p: %s" % repr(p))

s1 = "Point is:" + str(p)
print(s1)

print(p.__doc__)