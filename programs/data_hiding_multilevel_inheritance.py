class A:

    def __init__(self):
        print("A.__init__()")
        self.x = 10


class B(A):

    def __init__(self):
        print("B.__init__()")
        super().__init__()
        self.x = 20


class C(B):

    def __init__(self):
        print("C.__init__()")
        super().__init__()
        self.x = 30


class D(C):

    def __init__(self):
        print("D.__init__()")
        super().__init__()
        self.x = 40


class E(D):

    def __init__(self):
        print("E.__init__()")
        # super().__init__()
        # print("E - Assigning the x now")
        self.x = 50


e = E()
print(e.x)