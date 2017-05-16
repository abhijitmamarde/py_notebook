a = 4
b = 7.5

if (type(a) == type('')) and (type(b) == type('')):
    print("HEllo, Goodmorning")
    print(a)
    print(b)
elif ((type(a) == type(0) or type(a) == type(0.)) and (type(b) == type(0) or type(b) == type(0.))):
    print("addition of:")
    print(a)
    print(b)
    print("is:")
    print(a+b)
else:
    print("Both a and b should be either string or, either of, int and float")