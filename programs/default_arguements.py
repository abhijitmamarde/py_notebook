# will not work, once you start writing
# default args, all other args after it
# has to be mentioned as default args
# def add(n1, n2=0, n3=0, n4):

def add(n1, n2=0, n3=0, n4=0):
    print("sum:", (n1 + n2 + n3 + n4))

add(1,2,3,4)
add(1,2,3)
add(1,2)
add(1)
# add()  # will raise error, n1 is required


add(1, n3=10)

# variadic functoion
# function that can take N number of args
def add_v2(*args, **kwargs):
    print("inside add_v2()")
    print("args:", args)
    print("kwargs:", kwargs)
    sum = 0
    for i in args:
        sum += i

    for k, v in kwargs.items():
        if k.startswith('n'):
            sum += v

    print(sum)

add_v2(100,200,300,400,n1=1, n2=2, n3=3, n4=4, n5=5, n6=6, a=7, b=8, c=9, d=10)




# function clojures
def add_sub(n1, n2):
    def add(n1, n2):
        return n1+n2

    def subn(n1, n2):
        return n1-n2

    return (add(n1, n2), subn(n1, n2))

print(add_sub(n1=10, n2=5))

print(add(2,1))     # will call original add
# print(subn(5,2))  # will not work, subn is function clojure