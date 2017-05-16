# tuple is read-only list

# define empty tuple
t1 = ()
print(t1)
print(type(t1))
# or
t1 = tuple()
print(t1)
print(type(t1))

# defining tuple with values
t1 = ('a', 'e', 'i', 'o', 'u')
print(t1)
# is similar to
t2 = tuple('aeiou')
print(t2)
print(t1 == t2)



# operations
t1 = tuple('abhijit')
print(t1)
print(len(t1))
print(t1.count('i'))
print(t1.index('i'))

print(t1[0])
print(t1[6])


print(sorted(t1))

# list to tuple and vice versa possible
l1 = [1,2,3]
t1 = tuple(l1)
print(l1)
print(t1)

t1 = (4,5,6)
l1 = list(t1)
print(t1)
print(l1)

# iterable  usage in for loop
s1 = "abhijit"
l1 = list(sorted(s1))
t1 = tuple(sorted(l1, reverse=True))

for i in s1:
    print(i)
print()

for i in l1:
    print(i)
print()

for i in t1:
    print(i)
print()


# usage using while instead of for loop
i = 0
n = len(l1)
while  i < n:
    print(l1[i])
    i += 1


# define a string using list/tuple
# usage of join
l1 = ['Python', 'is', 'easy', 'to', 'learn']
print(l1)
t1 = ('Python', 'is', 'easy', 'to', 'learn')
print(t1)

print(' '.join(l1))
print(','.join(t1))

# this is how join works
# l1[0] + join_char + l1[1] + ... + join_char + l1[n]

l1 = ['a','b','c']
print(' '.join(l1))
print(l1[0] + ' ' + l1[1] + ' ' + l1[2])

# split a big string to a list with individual small list items
s1 = 'Python|is|easy|to|learn'
print(s1)
l1 = s1.split('|')
print(l1)

for word in l1:
    print(word)