#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# a=[1,[2,[3,[4,[5,[6]]]]]]

a = [
        1,
        [
            2,
            [
                3,
                [
                    4,
                    [
                        5,
                        [6]
                    ]
                ]
            ]
        ]
    ]

print(a)
#first element
print(a[0])
print(a[1][1][1][1][1][0])
print("The length is:",len(a))

a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)
print("The length is:",len(a))





# b = [1,2,3,4,5] 


# b = 1+2+3 + 2+3+4 + 3+4+5
# print b


print('-'*30)

# to get Help on list object
# >>> help([])


vowels1 = ['a', 'e', 'i', 'o', 'u']
vowels2 = list('aeiou')
print(vowels1)
print(vowels2)
print(vowels1 == vowels2)

vowels1.append('z')
print(vowels1)
print(vowels1 == vowels2)

print(len(vowels1))
vowels1.clear()
print(vowels1)
print(len(vowels1))


# list is mutable, string is not
print('-'*30)
l1 = [1,2,3]
l2 = l1
print(id(l1))
print(id(l2))
l1[0] = 10
print(l1)
print(l2)

# string is not mutable
s1 = "abhi"
s2 = s1
print(s1)
print(s2)
print(id(s1))
print(id(s2))

s1 += "!"
print(s1)
print(s2)
print(id(s1))
print(id(s2))



print('-'*30)
print(id(vowels1))
print(id(vowels2))
vowels1 = vowels2.copy()
print(vowels1)
print(id(vowels1))
print(id(vowels2))


# count(), extend() usage
print('-'*30)
l1 = [1,2,3,3,4,2,1,4,3,1]
l2 = ['a', 'b', 'c']
print(l1.count(1))
# append is not similar to extend
# l1.append(l2) 

# this would yield same o/p
l1.extend(l2) 
# l1.extend('abc')
# l1  += 'abc' 
print(l1)
print(l1.index(3))

l1 = list('abc')
print(l1)
print(len(l1))
print(id(l1))
print(l1.pop())
print(l1)
print(len(l1))
print(id(l1))



# usage of reverse(), sort(), sorted()