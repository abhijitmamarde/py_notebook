def hello():
    print(1)
    # recursion - function calling itself
    # hello()

hello()


def boom(n):
    if n == 0:
        print("BOOM!")
    else:
        print("Ticking...%d" % n)
        boom(n-1)

boom(1000)

