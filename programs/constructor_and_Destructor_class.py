class MyClass:

    def __init__(self, n):
        self.n = n
        print("__init__(%d) called" % self.n)

    def __del__(self):
        print("__del__(%d) called" % self.n)

a1 = MyClass(1)
a2 = MyClass(2)
a3 = MyClass(3)

# l = []
# for i in range(10,21):
#     l.append(MyClass(i))

for i in range(10,21):
    x = MyClass(i)
    if (i == 15) or (i == 17):
        del a1
        del a3
        a3 = MyClass(300+i)
        a1 = MyClass(100+i)
