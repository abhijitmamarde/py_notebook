class MyClass:

    def __init__(self, instance):
        self.instance = instance
        print("MyClass(%s) init is called" % self.instance)

    def __del__(self):
        print("MyClass(%s) del is called" % self.instance)

c1 = MyClass(instance="c1.1")
c2 = MyClass(instance="c2")
c1 = MyClass(instance="c1.2")
del c1
for i in range(5):
    print(".", end="")