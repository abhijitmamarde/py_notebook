s1 = "abhijit"
l1 = list(s1)
t1 = tuple(s1)

print(s1)
print(l1)
print(t1)

print(s1[1])
print(l1[1])
print(t1[1])

# slice  [start:end]
# start, end - index value
# start - inclusive
# end - exclusive
print(s1[0:2])
print(l1[0:2])
print(t1[0:2])

print(s1[1:5])
print(l1[1:5])
print(t1[1:5])

print(s1[len(s1)-2:len(s1)])
print(l1[len(l1)-2:len(l1)])
print(t1[len(t1)-2:len(t1)])

# default values for both start and end is define
# start - 0
# end - len of that object (str/list/tuple/set)
print(s1[len(s1)-2:])
print(l1[len(l1)-2:])
print(t1[len(t1)-2:])

print(s1[:len(s1)-2])
print(l1[:len(l1)-2])
print(t1[:len(t1)-2])


# both start and end could be negative
# when you pass negative, len(obj) - value
print(s1[:-2])
print(l1[:-2])
print(t1[:-2])

print(s1[-5:-2])
print(l1[-5:-2])
print(t1[-5:-2])


# quick way for copy of str, list, tuple, set etc.
s2 = s1[:]
l2 = l1[:]
t2 = t1[:]

print(s2)
print(l2)
print(t2)


# invalid index for start and end would not raise any error

s3 = "this is some string"
print(s3[-100:-50])