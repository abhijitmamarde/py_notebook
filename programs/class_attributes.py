class MyClass:

    # defining class attributes
    name = "This is name"
    count = 0

    def __init__(self):
        self.c = 0

    def incr(self):
        self.c += 1

    def print(self):
        print("Count is:%d" % self.c)
        print("Class attribute name:%s" % MyClass.name)
        print("Class attribute count:%d" % MyClass.count)



c1 = MyClass()
c1.print()

c1.incr()
c1.print()

# accessing instance attributes
print(c1.c)

# accessing class attributes
print(c1.name)
print(c1.count)

MyClass.count = 1
# accessing class attributes using Class name
# no need to have an instance in order to 
# access the class attributes
print(MyClass.name)
print(MyClass.count)

c1.print()
