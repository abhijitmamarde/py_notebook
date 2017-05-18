# split() and join() both are string methods

# split() - converts big-string to various small-strings
# based on some char
s1 = "My name is abhijit"
l1 = s1.split(" ")  # splits on char - space / ' '
print(l1)
print(type(l1))
print(len(l1))


# | char is delimeter
s2 = "abhijit mamarde|34|software engineer|python, c++, c, bash"
l2 = s2.split("|", maxsplit=1)  # splits on char - |
print(l2)
l2 = s2.split("|")  # splits on char - |
print(l2)
print(type(l2))
print(len(l2))


# join() - it will make a big string from the list of strings 
# and will concatenate strings using the char mentioned
l3 = ['abhijit mamarde', '34', 'software engineer', 'python, c++, c, bash']
s3 = "|".join(l3)
print(s3)
print(type(s3))


# join from two list
l4 = list("abc")
l5 = list("efg")
print(l4)
print(l5)
ttile = "".join(l4+l5)
print(ttile)
print("                   " + ttile + "                ")
print(ttile.center(50, '-'))

print("".join(list("abc") + list("def")).center(50,'+'))
