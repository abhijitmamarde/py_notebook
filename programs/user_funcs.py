# function 
# logical block of code
# it should do one thing , and only one thing well
# re-usability

# writing/defining func
# def keyword

def hello():
    pass

# calling function
hello()


def hello1():
    print("Hello World")
    print("how are you")



# calling function
hello1()
hello1()


# def and calling func with arguments
# usage of return keyword
def add(n1, n2):
    if not(type(n1) == type(int()) and type(n2) == type(int())):
        print("Can add two int values only")
        return

    sum = n1 + n2
    print("sum of two nums are: %d" % (sum))
    return sum

print("outside func ret val: add(1,2)=%d and add(4,5)=%d" % (add(1,2), add(4,5)))
print("outside func ret val: add(1,2)=" + str(add(1,2)) + " and add(4,5)=" + str(add(4,5)))

number1 = 20.7
print(add(number1, 100))

number1 = "hey"
print(add(number1, 'there'))




def add_and_sub(n1,n2):
    print("add_and_sub is called")
    return (n1+n2, n1-n2)


# print("add of 10, 3 is: %d and sub is: %d" % (add_and_sub(10, 3)[0], add_and_sub(10, 3)[1]))
v1, v2 = add_and_sub(10, 3)
print(v1)
print("add of 10, 3 is: %d and sub is: %d" % (v1, v2))

# print(add_and_sub(6, 10))




def avg_list(l1):
    sum = 0
    l2 = []
    for i in l1:
        sum += i*i
        l2.append(i*i)
    return (sum/len(l1), l2)

l2 = [1,2,3,4,5]
avg, sq_list = avg_list(l2)
print("Avg of list: %s is: %f" % (sq_list, avg))


def swap(a, b):
    return (b,a)

a = 10
b = 20
print(a, b)
# a, b = swap(a, b)
a, b = (b, a)
print(a, b)


def swap2(a, b):
    print("Inside swap2", id(a), id(b))
    # temp = a
    # a = b
    # b = temp
    a +=1
    b +=1
    print("Inside swap2, after", id(a), id(b))
    print("Inside swap2, a,b is: ", a, b)
    return (a,b)


a = 10
b = 20
print("before/outside id:", id(a), id(b))
print(swap2(a, b))
print("after/outside id:", id(a), id(b))
print(a, b)


def inc_list(l1, n):

    for i in l1:
        print(i)

    # enumerate would give index pos along with value
    # index pos would always start from 0 to len(obj)-1
    for i, num in enumerate(l1):
        l1[i] = num + n

    print("inside func:", l1)
    return l1

l2 = [1,2,3,4,5]
print(inc_list(l2, 3))
print(l2)


def sum_list(l1):
    sum = 0
    for i in l1:
        sum += i
    return sum

l1 = [1,2,3,4,5]
# print(sum_list(l1))

# speed optimatizaion technique
print(sum_list(tuple(l1)))


# 0 1 1 2 3 5 8 13 21 ...
def fib(n):
    # print(n)
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(10))


def a():
    b()

def b():
    c()

def c():
    a()


# would raise Reciussison error - indirect recusion
# b()

# functions are first class citizen in Python
# they are treated the same way as other identifiers/variables
# function can be passed to functions
# function can return the function

def sq(n):
    return n*n

def cube(n):
    return n*n*n

def calculate(f, n):
    return f(n)  # only function obj is callable

print(sq(2))
print(calculate(sq, 2))
print(calculate(cube, 2))

# print(calculate(list(), 2))  # only function obj is callable


# clojures
def add(n1, n2):
    def sub(n1, n2):
        return n1 - n2
    return (n1 + n2, sub)

sumval, fsub = add(3,4) 
print(type(fsub))
diffval = fsub(3,4)
print(sumval, diffval)



# monkey - patching
def mytype(obj):
    s1 = "%s" % type(obj)
    print(s1.upper())
    print("-"*len(s1))

print(type(mytype))
# print(mytype(mytype))

# def set_type(hack=True):
#     def mytype(obj):
#         s1 = "%s" % type(obj)
#         print(s1.upper())
#         print("-"*len(s1))
#     if hack:
#         _type = type
#         type = mytype
#         return (_type, mytype)
#     else:
#         type = _type
#         return (_type, mytype)

# print("="*40)
# print(type(mytype))
# set_type(hack=True)
# print(type(mytype))






def sum_def(n1, n2, n3=0, n4=0, n5=0, n6=0):
    sum = n1 + n2 + n3 + n4 + n5 + n6
    return sum

print(sum_def(1,2,3,4))
print(sum_def(1,2,n6=20, n5=15))
# print(sum_def())