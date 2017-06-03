class Counter:

    count = 0

    def __init__(self):
        self.c = 0

    def incr(self):
        self.c += 1
        Counter.count += 1

    def print(self):
        print("Instance count is:%d" % self.c)
        print("Class count is:%d" % Counter.count)
        print("-----")


c1 = Counter()
c1.incr()
c1.incr()
c1.print()

c2 = Counter()
c2.incr()
c2.incr()
c2.print()

c3 = Counter()
c3.incr()
c3.incr()
c3.print()

# remember here, no new instance is getting created
# so init/constructor is not getting called
# and instance attribute c is not 
# getting re-initialize/defined with 0
c1.incr()
c2.incr()
c3.incr()
c1.print()

