class MyClass:
	pass

# class MyClass():
# 	pass

# class MyClass(MyParentClass1):
# 	pass

# class MyClass(MyParentClass1, MyParentClass2):
# 	pass

# obj = MyClass
obj = MyClass()


class Point:

	system = "2D"

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.quadrant = 1
		# print("init is called for Point(%d, %d)" % (self.x, self.y))

	def __del__(self):
		# print("del is called for Point(%d, %d)" % (self.x, self.y))
		pass

	def __add__(self, p2):
		print("add called")
		# print("Calculating add of:")
		# self.show()
		# p2.show()
		if isinstance(p2, Point):
			return Point(self.x + p2.x, self.y + p2.y)
		elif isinstance(p2, int):
			return Point(self.x + p2, self.y + p2)

	def __radd__(self, p2):
		print("radd called")
		return Point(self.x + p2, self.y + p2)

	def __len__(self):
		return self.x + self.y


	def show(self):
		print("Point(%d, %d)" % (self.x, self.y))

	def help():
		print("Type for simulating Point in a %s system/coordinates" % Point.system)

	@staticmethod
	def stat_func():
		print("Called a stat_func() of Point %s" % Point.system)

	@classmethod
	def class_func(cls):
		print("Called a class_func() of Point %s" % cls.system)

# p1 = Point()
# p2 = Point(1,1)
# p3 = Point(1,2)

# del p2



# for i in range(11, 21):
# 	x = Point(i, i)


point1 = Point(1,2)
point2 = Point(3,5)

i = 10
j = 20

i + j 
p3 = point1 + point2
p4 = point1 + i
p5 = i + point1
# point3 = point1 + point2
# point3.show()

p3.show()
p4.show()
p5.show()

print(len(p3))
print(len(p4))
print(len(p5))

print("-"*40)

Point.help()
print(Point.system)
Point.stat_func()
Point.class_func()

print("Terminating...")

