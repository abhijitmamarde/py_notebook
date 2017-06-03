def add_v1(n1, n2):
    sum = int(n1) + int(n2)
    return sum


def add_v2(n1, n2):

    try:
        sum = int(n1) / int(n2)
        return sum
    except ValueError as err:
        print(err)
        print("Either n1 or n2 is not passed as int")
    except Exception as err:
        print(err)
        print(type(err))
        print("Unknown exception occured")

# print(add_v1(1,2))
# print(add_v2(1,2))

# print(add_v1("1","2d"))
# print(add_v2("1","2"))


def add_v3(n1, n2):
    if not(isinstance(n1, int) and isinstance(n2, int)):
        raise ValueError

    return n1+n2

try:
    print(add_v3(1,"2"))
    try:
        a =1 
    except:
        pass
except ValueError:
    print("ValueError in args for add_v3")
    print("Trying again...")
    try:
        print(add_v3("1d",2))
    except ValueError:
        print("Failed again with: ValueError in args for add_v3")

    


print("....End....")