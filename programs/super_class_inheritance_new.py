class A(object):
    def __init__(self):
        self.n1 = 1
        self.n2 = 2
        print('A.__init__')
        super().__init__()

    def comm(self):
        print("A.comm()")


class B(object):
    def __init__(self):
        self.n3 = 3
        self.n4 = 4
        print('B.__init__')
        super().__init__()

    def comm(self):
        print("B.comm()")


class C(B, A):
    def __init__(self):
        self.z = 100
        print('C.__init__')
        super().__init__()

    def show(self):
        print("4 nums are: %d %d %d %d" % (self.n1, self.n2, self.n3, self.n4))


c = C()
c.show()
c.comm()
print(C.__mro__)
# for c in C.mro():
#     print(c.__name__)