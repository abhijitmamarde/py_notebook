'''
Sample program to process the inputs in Threads, in:
the order in which the data is added to queue (FIFO order)  OR
in some specific order using: Priority Queue
'''
from queue import PriorityQueue, Queue
from threading import Thread, Lock
from time import sleep
from random import randint


class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def show(self): 
        print("Employee(name='%s', salary=%.2f)" % (self.fname + ' ' + self.lname, self.salary))

    def __lt__(self, e2):
        # comparing two objects based on salary, 
        # higher salary gets more priority
        return self.salary > e2.salary
        # comparing two objects based on lname, 
        # priority will be given based on ascending order for lname
        # m will come first than n
        # return self.lname < e2.lname

 
class MyThread(Thread):
    def __init__(self, thread_id, name, q):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = name
        self.q = q
    
    def run(self):
        print("Starting Thread: " + self.thread_name)
        self.process_data()
        print("Exiting Thread: " + self.thread_name)
 
    def process_data(self):
        while not exit_flag:
            queue_lock.acquire()
            if not work_queue.empty():
                data = self.q.get()
                queue_lock.release()
                # print("%s processing: %s" % (self.thread_name, data))
                print("%s processing:" % (self.thread_name))
                data.show()
            else:
                queue_lock.release()
            sleep(randint(0, 3))

if __name__ == "__main__":
    exit_flag = False
    thread_names = ["Thread-1", "Thread-2", "Thread-3"]
    
    # thread_data = ["One", "Two", "Three", "Four", "Five"]
    # thread_data = [10, 3, 6, 2, 7, 9, 1, 2, 11, 18, 21, 8, 16, 12]
    thread_data = [
        Employee('abhi', 'm', 25.5),
        Employee('mangesh', 'n', 23.4),
        Employee('nitin', 'k', 27.0),
    ]

    queue_lock = Lock()
    # this is normal FIFO queue, data will be processed in same order
    # work_queue = Queue() 

    # in PriorityQueue, data will be processed with priority (__cmp__) lowest values first!
    work_queue = PriorityQueue() 
    
    threads = []
    thread_id = 1
    
    # Create new threads
    for thread_name in thread_names:
        thread = MyThread (thread_id, thread_name, work_queue)
        thread.start()
        threads.append(thread)
        thread_id += 1
    
    print("Writing data to work queue...")
    # Fill the queue
    queue_lock.acquire()
    for data in thread_data:
        work_queue.put(data)
        sleep(0.5)
    queue_lock.release()
    print("Work queue generated...Done")
    
    # Wait for queue to empty
    while not work_queue.empty():
        pass
    
    # Notify threads it's time to exit
    exit_flag = True
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")