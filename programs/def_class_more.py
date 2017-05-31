class MyClass1:

    def __init__(self, a=10, b=20):
        print("Called init")
        self.x = a
        self.y = b
        self.z = ''


a = MyClass1()
b = MyClass1(30, 40)

print(a.x, a.y)
print(b.x, b.y)

print(a.z)
