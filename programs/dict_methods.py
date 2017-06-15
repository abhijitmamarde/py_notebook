# two ways for defn dict
d = dict()
print( type(d) )

d = {}
print( type(d) )

# dict is key value pair
d = {'name': 'abhijit', 'age': 24, 'is_student': False, 'salary': 24.5}

# key could be anyone of an int, float, bool, string or tuple but NOT list
# value could be any object/type in Python

# ----- basic operations  ------
print( len(d) )

# accessing items in a dict, using key
print( d['name'] )

# changing data for a particular key
d['name'] = "sachin"
print( d['name'] )

# adding a key value pair
print( d )
d['department'] = "IT"
print( d )

# deleting a key value pair
print( d['is_student'] )
del d['is_student']
# print( d['is_student'] )        # raises KeyError: 'is_student', as this key is no more available in dict

# checking availibility of a key
# check if a exists in dict or not
if 'salary' in d:
    print("Salary exists: ", d['salary'])
if 'is_student' in d:
    print("is_student exists: ", d['is_student'])
else:
    print("is_student does not exists: ")

# shortcut for doing same, get() method returns None if key is not found or return's the key's value
# the second argument defines the default value which will return in case key is not found (default value is None)
x = d.get('x', 0)
# x = d.get('salary')
print('x is:', x)


# --------- other methods of dict -----------
# help(dict())

# clear(), copy()
# same as that of list methods

# keys(), values() and items()
print("keys are:")
print(list(d.keys()))
for key in d.keys():
    print(key, d[key])


print("values are:")
print(list(d.values()))


print("items are:")
print(list(d.items()))
for k, v in d.items():
    print(k, v)



# pop(), popitem()
print(d)
print( d.pop('salary') )
print(d)

# print( d.pop('salary') )  # raises KeyError
print( d.pop('salary', 0) )  
print(d)


print(d.popitem())
print(d.popitem())
print(d.popitem())
# print(d.popitem()) # KeyError: 'popitem(): dictionary is empty'


# update()
d1 = {'a': 1, 'b': 2}
d2 = {'a1': 11, 'b1': 12}
d3 = {}
# similar to operation d3 = d1 + d2 
# but '+' operator does not work for dict object
d3.update(d1)
d3.update(d2)
print(d3)
