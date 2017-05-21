# os_walk_demo.py

import os
import os.path

w = os.walk(".")
print(type(w))

for r, subdirs, files in w:
    # print(r)
    # print(subdirs)
    # print(files)
    for f in files:
        if f.endswith(".py"):
            print(r + os.path.sep + f)
    # print("-"*30)