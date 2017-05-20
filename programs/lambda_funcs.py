def sq(n):
    return n*n

print(sq(2))

g = lambda n: n*n
print(type(sq))
print(type(g))

print(g(3))

add_and_sub = lambda n1, n2: (n1+n2, n1-n2)
add, sub = add_and_sub(n2=10, n1=7)

print(add, sub)


def calculte(f1, n1, n2):
    return f1(n1, n2)

# def add(n1, n2):
#     return n1+n2

# def sub(n1, n2):
#     return n1-n2

# print(calculte(add, 1, 2))
print(calculte((lambda n1,n2: n1+n2), 30, 40))
print(calculte((lambda n1,n2: n1-n2), 30, 40))
print(calculte((lambda n1,n2: n1*n2), 30, 40))
print(calculte((lambda n1,n2: n1/n2), 30, 40))

data_processors = [
    lambda n1,n2: n1+n2,
    lambda n1,n2: n1-n2,
    lambda n1,n2: n1*n2,
    lambda n1,n2: n1/n2,
]


data_pipeline = [0,1,1,1,3,3,3,3,1,2,3,0,2,3,1]
sn1, sn2 = (10, 20)
sum = 0
for m in data_pipeline:
    sum += calculte(data_processors[m], sn1, sn2)
    sn1 = sum
    sn2 = sn1 * 10

print(sum)