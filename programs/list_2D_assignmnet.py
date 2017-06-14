'''
Program to calculate the sum (row, col) for a 2D list

ex:

if input list is:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

then output should be:

1, 2, 3 sum = 5
4, 5, 6 sum = 15
7, 8, 9 sum = 24
Col sum=12, 15, 18
]
'''

l1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

csum = [0] * len(l1)
print(csum)
for i in l1:
    rsum = 0
    for index, j in enumerate(i):
        print(j, end=",")
        csum[index] += j
        rsum += j
    print("sum =", rsum)

print(l1)
print(csum)


