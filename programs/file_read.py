# f = open("sample_read_file.txt")
# f = open("./pack1/sample_read_file.txt")
f = open("/Users/abhijitmamarde/pwork/py_notebook/programs/pack1/sample_read_file.txt", "r")
print(type(f))

# data = f.read()
# print(type(data))
# print(data)


data = f.readlines()
print(type(data))
print(data)

data_stripped = []
for x in data:
    l = x.strip()
    if l:
        data_stripped.append(l)

print(data_stripped)