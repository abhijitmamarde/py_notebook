class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        if x < 0:
            if y < 0:
                self.quadrant = 3
            else:
                self.quadrant = 2
        else:
            if y < 0:
                self.quadrant = 4
            else:
                self.quadrant = 1

    def __lt__(self, arg1):
        if isinstance(arg1, Point):
            return self.quadrant < arg1.quadrant
        elif isinstance(arg1, int):
            return self.quadrant < arg1


p1 = Point(10, 2)
p2 = Point(10, -2)

print(p1 < p2)
print(p2 < p1)


print(p1 < 2)
print(p2 < 4)

