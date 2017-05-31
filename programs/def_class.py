# defining class
class MyClass:
    pass

# class MyDerivedClass(MyClass, MyClass2, MyClass3)
class MyDerivedClass(MyClass):
    pass


print(type(MyClass))
print(type(MyDerivedClass))

# create instance / object
c1 = MyClass()
c2 = MyDerivedClass()

print("Instance c1 type:", type(c1))
print("Instance c2 type:", type(c2))

# once a blueprint (class) is created, we can
# create multiple buildings (object/instance) out of it
# id for every object/instances are different
c11 = MyClass()
c12 = MyClass()
c13 = MyClass()
c14 = MyClass()
c15 = MyClass()


print("id(c11)=", id(c11))
print("id(c12)=", id(c12))
print("id(c13)=", id(c13))
print("id(c14)=", id(c14))
print("id(c15)=", id(c15))

print("-"*10)

class Point:

    # init is constructor for your class
    # called automatically during 
    # creation of object
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.calc_quadrant()

    def print(self):
        print(id(self))
        print("Point x:%d, y:%d, Quadrant: %d" % (self.x, self.y, self.quadrant))

    def calc_quadrant(self):
        if self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x >= 0 and self.y < 0:
            self.quadrant = 4
        elif self.x >= 0 and self.y >= 0:
            self.quadrant = 1
        else:
            self.quadrant = 2



p = Point()
print(id(p))
# print("Point p is:  ", p)
# p.calc_quadrant()
p.print()
print(p.x, p.y)

p2 = Point(10, -20)
p2.print()



# class Point3d(Point):

#     def __init__(self, x=1, y=2, z=3):
#         Point.__init__(self, x, y)
#         self.z = z

#     def print(self):
#         print("Point 3d: x=%d, y=%d, z=%d, quadrant=%d" % (self.x, self.y, self.z, self.quadrant))


# p3d1 = Point3d(-4, -5, 1)
# p3d1.print()

# p3d2 = Point3d()
# p3d2.print()




# class A:
#     def __init__(self):
#         self.i = 10
#         self.data = 20

# class B:
#     def __init__(self):
#         self.j = 20
#         self.data = 40


# class C(B, A):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)

#     def print(self):
#         print(self.i, self.j, self.data)


# c = C()
# c.print()

# print(c.__mro__)