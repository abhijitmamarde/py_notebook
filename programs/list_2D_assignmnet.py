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
[
[1,   2,  3,  5],
[4,   5,  6, 15],
[7,   8,  9, 24],
[12, 15, 18, -1]
]
'''

l1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# csum = [0] * len(l1)
# print(csum)
# for i in l1:
#     rsum = 0
#     for index, j in enumerate(i):
#         print(j, end=",")
#         csum[index] += j
#         rsum += j
#     print("sum =", rsum)

# print(l1)
# print(csum)

resl = l1.copy()
resl.append([0]*3)

for ind1, i in enumerate(l1):
    rsum = 0
    for ind2, j in enumerate(i):
        resl[3][ind2] += j
        rsum += j
    resl[ind1].append(rsum)

resl[3].append(-1)
print(resl)