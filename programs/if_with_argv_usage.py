import sys

print("The argv which you have passed is:")
print(sys.argv)

print("the age youu entered is:")
print(sys.argv[1])

q = sys.argv[1]
n = int(q)

if n < 18:
    print("Can not vote")
else:
    print("Can vote now.")

print("done.")