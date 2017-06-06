class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def comapre_with_point(self, p2):
        if (self.x <= p2.x) and (self.y <= p2.y):
            return True

        return False

    def __lt__(self, p2):
        if isinstance(p2, Point) and (self.x <= p2.x) and (self.y <= p2.y):
            return True
        elif isinstance(p2, int) and (self.x <= p2):
            return True
        elif isinstance(p2, tuple) and (len(p2) >= 2) and (self.x <= p2[0]) and (self.y <= p2[1]):
            return True

        return False

p1 = Point(100, 2)
p2 = Point(120, 3)
print(p1 < p2)
print(p1.comapre_with_point(p2))

print(p1 < 100)
print(p2 < 100)

print(p2 < (100,300))


# <     __lt__
# <=    __le__
# >     __gt__
# >=    __ge__
# !=    __ne__
# ==    __eq__
