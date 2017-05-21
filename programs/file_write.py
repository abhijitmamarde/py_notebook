name = input("Enter name:")
# f = open("./pack1/sample_read_file.txt", "w")  #w - write mode, overwrites
f = open("./pack1/sample_read_file.txt", "a")    #a - append mode, not overwites
written = f.write(name+"\n")
print("File written:", written)