class B:

    @classmethod
    def foo(obj):
        print("B's foo() called")

class D(B):
    # pass
    
    @classmethod
    def foo(obj):
        print("D's foo() called")

D.foo()