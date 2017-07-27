class Shape:

	def __init__(self, sides=0):
		self.sides = sides


	def area(self):
		print("Calculating area of shape with side: %d" % self.sides)
		# print("Area of shape is:")


class Circle(Shape):

	def __init__(self, radious, sides=0):
		self.radious = radious
		super().__init__(sides)

	def show(self):
		print("Circle(radious=%d)" % self.radious)
		super().area()




class Square(Shape):

	def __init__(self, length, sides=4):
		self.length = length
		self.sides = 4
		super().__init__(sides)


	def show(self):
		print("Square(len=%d)" % self.length)
		self.area()




s1 = Circle(10)
s2 = Square(20)

s1.show()
s2.show()