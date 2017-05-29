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

myCount10 = MyThreadCount("Thread1", 10)
myCount30 = MyThreadCount("Thread2", 30)
myCount50 = MyThreadCount("Thread3", 50)

myCount10.start()
myCount30.start()
myCount50.start()