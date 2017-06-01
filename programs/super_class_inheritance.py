class A(object):
    def __init__(self, x, y):
        self.n1 = x
        self.n2 = y
        print('A.__init__')
        super().__init__(x, y)


class B(object):
    def __init__(self, x, y):
        self.n3 = x
        self.n4 = y
        print('B.__init__')
        super().__init__()


class C(A, B):
    def __init__(self, x, y, z):
        self.z = 100
        print('C.__init__')
        super().__init__(x, y)

    def show(self):
        print("4 nums are: %d %d %d %d" % (self.n1, self.n2, self.n3, self.n4))


c = C(1,2,3)
c.show()
for c in C.mro():
    print(c.__name__)