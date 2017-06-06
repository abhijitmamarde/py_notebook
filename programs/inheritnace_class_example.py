class Car:

    def __init__(self):
        print("Car.__init__() called")
        self.color = "white"
        self.doors = 4


class Ritz(Car):
    
    pass
    def __init__(self):
        # Car.__init__(self)
        super().__init__()
        print("Ritz.__init__() called")
        self.color = "red"


c1 = Car()
print(c1.color)
print(c1.doors)

c2 = Ritz()
print(c2.color)
print(c2.doors)
