import builtins

s1 = "String with num: 1234"
print("s1:", s1)
print("Before patch len(s1):", len(s1))
    
# orig_len = len

def mylen(obj):
    print("mylen called!")
    return builtins.orig_len(obj) + 1

# len = mylen

def patch_len():
    builtins.orig_len = builtins.len
    builtins.len = mylen

def unpatch_len():
    builtins.len = builtins.orig_len
    del builtins.orig_len

patch_len()

print("After  patch len(s1):", len(s1))

unpatch_len()

print("After  unpatch len(s1):", len(s1))