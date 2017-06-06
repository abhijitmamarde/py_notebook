import threading
import time

class MyThreadCount(threading.Thread):
    
    def __init__(self, name, number): 
        threading.Thread.__init__(self)
        self.count = number
 
    def run(self): 
        for i in range(self.count):
            print("Thread: %s i: %d" % (self.name, i))
            time.sleep(1)

myCount1 = MyThreadCount("Thread1", 1)
myCount2 = MyThreadCount("Thread2", 3)
myCount3 = MyThreadCount("Thread3", 5)

myCount1.start()
myCount2.start()
myCount3.start()