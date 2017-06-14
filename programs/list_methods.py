# list is hetrogenous container
# can have/store ANY object

l1 = [1, 'str1', 3.5, True, False, [1,2,3], 9]


# list elemnets are accessed using index of operator - []
# list indexes as with array indexes in other language start from 0
print(l1[0])  # 1
print(l1[1])  # str1
print(l1[5])  # [1,2,3]
# print(l1[7])  # will raise exception IndexError

# array index values could be negatives

print(l1[-1])  # 9  (the last element)
print(l1[-2])  # [1,2,3]  (the last second element)
print(l1[-7])  # 1  (the last seventh element, which is also first element in this case)
# print(l1[-8])  # will raise exception IndexError


l2 = [1,2,3]
print(l2)   # [1, 2, 3]
l2[0] = 10
print(l2)   # [10, 2, 3]


l3 = [[1,2,3], [4,5,6], [7,8,9]]
print(l3)        # [[1,2,3], [4,5,6], [7,8,9]]
l3[2][2] = 100
print(l3)        # [[1,2,3], [4,5,6], [7,8,100]]



# operators on list
print(len(l3)) # 3
l4 = [5,6,7]
l5 = [8,9,10]

l4 = l4 + l5    # list concatenate
print(l4) # [5,6,7,8,9,10]


l6 = [1,3,4] * 3    # list repetation operator
print(l6)   # [1, 3, 4, 1, 3, 4, 1, 3, 4]


l7 = [1,2,3]
print(l7)       # [1,2,3]
del l7[1]       # del list element
print(l7)       # [1,3]


# sort
l8 = [3,4,2,1,5]
print(l8)           # [3,4,2,1,5]
print(sorted(l8))   # [1,2,3,4,5]
print(sorted(l8, reverse=True))   # [5, 4, 3, 2, 1]
print(l8)           # [3,4,2,1,5]



# other operations / methods of list object:
# help(list()) on python interactive prompt


# append(obj) - adds element at end of list
l9 = [1,2,3]
l9.append(10)
l9.append(11)
l9.append(13)
l9.append(12)
print(l9)   # [1,2,3,10,11,13,12]
l9.append([100,200])
print(l9)   # [1,2,3,10,11,13,12,[100,200]]

# extend() - extends list with another list items
l9.extend([300, 400])
print(l9)   # [1,2,3,10,11,13,12,[100,200],300,400]


# clear() - removes all items from the list
l9.clear()
print(l9)  # []


# count(value) - gives how many times an element is found in list
l10 = [1,2,3,4,5,3,4,6,5,3,5,7,4,2,3,3,2,1]
print(l10.count(2)) # 3
print(l10.count(1)) # 2
print(l10.count(100)) # 0


# index(value) - it gives first index position where the given element is found
print(l10.index(5)) #4
print(l10.index(7)) #11
# print(l10.index(100)) #ValueError: 100 is not in list

# insert(index, newval) - allows to insert the element at particular index pos
l11 = [1,2,3]
l11.insert(1, 11)  # [1, 11, 2, 3]
print(l11)
l11.insert(100, 99)  # [1, 11, 2, 3, 99]   ; NO IndexError Raised

# pop([index]) - removes the last element from the list and return the elements
l12 = [1,2,3]
print(l12.pop())    # 3
print(l12)          # [1, 2]
print(l12.pop(0))    # 1
print(l12.pop(0))    # 2
# print(l12.pop())    # IndexError: pop from empty list

print(l12)          # []


# remove(value) - removes search the value in list and removes first matching value from the list
l13 = [1,2,3,2,1]
l13.remove(3)
print(l13) # [1, 2, 2, 1]
l13.remove(1)
print(l13) # [2, 2, 1]


# sort(), reverse()
l14 = [8,1,2,7,3,2,5,6,1]
print(l14)   # [8,1,2,7,3,2,5,6,1]
l14.sort()
# l14.sort(reverse=True)
# l14.reverse()
print(l14)   # [1, 1, 2, 2, 3, 5, 6, 7, 8]




# copy() - does the deepcopy of the list rather than just copying the reference
# id()  - is a builtin function, which returns the memory address where the given object is stored
l15 = [1,2,3]
l16 = l15       # this will copy the reference l15 to l16
print(id(l15))  # i.e id(l15) == id(l16)
print(id(l16))
print(l15)  # [1, 2, 3]
print(l16)  # [1, 2, 3]
l15[0] = 11
print(l15)  # [11, 2, 3]
print(l16)  # [11, 2, 3]
l16[1] = 12
print(l15)  # [11, 12, 3]
print(l16)  # [11, 12, 3]

l15 = [1,2,3]
l16 = l15.copy()    # this will create a new list object based on l15 and then assign its reference to l16
print(id(l15))      # therefore, the ids of l15 and l16 would be different
print(id(l16))
print(l15)  # [1, 2, 3]
print(l16)  # [1, 2, 3]
l15[0] = 11
print(l15)  # [11, 2, 3]
print(l16)  # [1, 2, 3]
l16[1] = 12
print(l15)  # [11, 2, 3]
print(l16)  # [1, 12, 3]


# for loop for list object

for i in [1,2,3,4,5]:
    print(i)

l1 = [1,2,3,4,5]
for i in l1:
    print(i)


l2 = [[1,2,3], [4,5,6], [7,8,9]]
for i in l2:
    for j in i:
        print(j, end=",")
    print()
