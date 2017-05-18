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

add(1,2)

number1 = 20.7
add(number1, 100)

number1 = "hey"
add(number1, 'there')

