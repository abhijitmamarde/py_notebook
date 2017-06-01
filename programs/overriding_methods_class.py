

class MyClass:

    def add(self, x, y):
        print("MyClass.add(%d, %d)= %d" % (x, y, x+y))


class MyDerivedClass(MyClass):

    def sub(self, x, y):
        print("MyDerivedClass.sub(%d, %d)= %d" % (x, y, x-y))

    # overriding the add method of Parent class
    def add(self, x, y):
        print("MyDerivedClass.add(%d, %d)= %d" % (x, y, x-y))



c1 = MyClass()
c1.add(3,4)

# c2 = MyDerivedClass()
# c2.add(50,35)
# c2.sub(40,30)

c2 = MyDerivedClass()
c2.add(3,4)
c2.sub(40,30)


# O/p when add() is not override in child class
'''
MyClass.add(3, 4)= 7
MyClass.add(50, 35)= 85
MyDerivedClass.sub(40, 30)= 10
'''

# on overriding O/p is:
'''
MyClass.add(3, 4)= 7
MyDerivedClass.add(50, 35)= 15
MyDerivedClass.sub(40, 30)= 10
'''

