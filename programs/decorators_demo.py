# function are first class citizen in Python
# can be used anywhere where an indetifier could be used
# passed to functions, return from functions etc.

def logusage(f):
    def function_wrapper(*args, **kwargs):
        print("="*30)
        print("calling function: %s" % f.__name__)
        print("args=%s, kwargs=%s" % (args, kwargs))
        retval = f(*args, **kwargs)
        print("finished: %s, retval is: %s" % (f.__qualname__, retval))
        return retval
    return function_wrapper

@logusage
def foo(n1, n2):
    print("foo is called")
    return n1+n2

@logusage
def bar(n1, n2=0, msg="hello"):
    print("bar is called")
    return msg + str(n1+n2)

s = foo(10, 20)
print("sum:", s)
m = bar(5, msg="World")
print("msg:", m)