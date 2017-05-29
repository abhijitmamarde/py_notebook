import pickle

# i = 10
# b = True
# f = 3.5

# l = [1,2,3,4]
# t = (6,7,8,9)
# d = dict(a=1, b=2, c=3)

# o = [i, b, f, l, t, d]
# fw = open("testpickle.bin", "wb")
# pickle.dump(o, fw)


fr = open("testpickle.bin", "rb")
o = pickle.load(fr)
print("Object read")
print(o)