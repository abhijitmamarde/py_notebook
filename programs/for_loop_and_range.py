# range funcs takes 3 vals:
# end
# start, end
# start, end, step
# start - is inclusive
# end - is exclusive
print(range(10))
print(list(range(10)))

print(range(1, 10))
print(list(range(1, 10)))

print(range(1, 10, 2))
print(list(range(1, 10, 2)))


for i in range(10, 0, -1):
    print(i)


# sample program using while loop
sum = 1
i = 1
while i <= 10:
    sum += i
    i += 1
print(sum)


# same sample program using for loop
sum = 1
for i in range(1, 11):
    sum += i
print(sum)

# sample while loop usage which can not be written using for loop
sum = 0
n = 0
while n >= 0:
    sum += n
    n = int(input("Enter the num (enter -1 to exit):"))
    print("adding n: %s to sum: %d" % (n, sum))
print(sum)