class MyClass:

    def __init__(self):
        print("MyClass.__init__()")
        self.x = 10


class MyDerivedClass(MyClass):

    # if below code is commented, 
    # c2.x is used from MyClass

    def __init__(self):
        super().__init__()
        print("MyDerivedClass.__init__()")

        # below line is 'hiding' the data attribute x
        # defined in base class
        self.x = 20




c2 = MyDerivedClass()
print(c2.x)

c1 = MyClass()
print(c1.x)




