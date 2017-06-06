class A:
    def __init__(self):
        self.a = 'a'
        self.common = 'a'

class B(A):
    def __init__(self):
        super().__init__()
        self.b = 'b'

class C(A):
    def __init__(self):
        super().__init__()
        self.c = 'c'


# class D(B, C):
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
class D(C, B):
    # [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
    def __init__(self):
        super().__init__()
        self.d = 'd'


b = B()
print(b.a, b.b, b.common)

c = C()
print(c.a, c.c, c.common)


d = D()
print(d.a, d.b, d.c, d.common)

print(D.mro())