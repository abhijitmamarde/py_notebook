import math
n = '3'
this_is_my_long_var1 = int()
this_is_my_long_var2 = int()
this_is_my_long_var3 = int()
this_is_my_long_var4 = int()
this_is_my_long_var5 = int()
this_is_my_long_var6 = int()

if type(n) == type(''):
    # n = int(n)
    print("its conerted to int")
    print(n)

if type(n) == type(1.):
    # n = math.floor(n)
    n = int(n)
    print("its conerted to int")
    print(n)
    
if True: #type(n) == type(0):
    print ("your age is:")
    print (n)
    print("you will celebrate your golden century in coming years")
    print(100-n)