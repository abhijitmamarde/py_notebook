# write_and_then_read_file.py

filename = "write_read_sample.txt"
fw = open(filename, "w")
l1 = [1,2,3,5,6,4,6,4,32,4]
for i in l1[:-1]:
    fw.write(str(i)+",")

fw.write(str(l1[-1]) + "\n")


# required to flush the buffere writes
# to save in disk
fw.close()

fr = open(filename, "r")
data = fr.read()
fr.close()
print(data)
l2 = []
for n in data.split(","):
    l2.append(int(n))

print(l2)
print(l1 == l2)

