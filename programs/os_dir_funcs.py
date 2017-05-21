import os

cwd = os.getcwd()
user=os.getlogin()
print("User:", user)
os.environ["mynam"] = "test"
home = os.getenv("mynam")
print("User home:", home)

if cwd.endswith("programs"):
    print("Current dir:", cwd)
    dirs = os.listdir()
    # print("dirs are:")
    # print(dirs)
    for l in dirs:
        print(os.stat(l))
else:
    print("Can-not execute program")


import datetime
t = datetime.datetime.fromtimestamp(1495362486)
print(t)


