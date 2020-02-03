from threading import Barrier, Thread,Lock

class Counter(object):
    def __init__(self):
        self.count=0

    def increment(self,offset):
        self.count += offset

class LockingCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count=0

    def increment(self,offset):
        # with self.lock:
        #     self.count += offset
        self.lock.acquire()
        self.count += offset
        self.lock.release()

def worker(how_many_increments, counter):
    BARRIER.wait()
    for _ in range(how_many_increments):
        counter.increment(1)


def run_threads(func,numb_threads, how_many_increments,counter):
    threads = []
    for i in range(numb_threads):
        args = (how_many_increments,counter)
        thread = Thread(target=func,args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

how_many_increments = 100000
numb_threads = 5
def act1():
    print('We are all off!')
BARRIER = Barrier(numb_threads, action = act1, timeout = None)

import timeit

counter = LockingCounter()
starttime = timeit.default_timer()
run_threads(worker,numb_threads,how_many_increments,counter)
tme  = (timeit.default_timer()-starttime)
print("time to run with locks:%1.3f" %tme )
print('Counter value should be %d ifound %d \n\n'% (how_many_increments*numb_threads,counter.count))



counter = Counter()
starttime = timeit.default_timer()
run_threads(worker,numb_threads,how_many_increments,counter)
tme  = (timeit.default_timer()-starttime)
print("time to run withOUT locks:%1.3f" %tme )
print('Counter value should be %d ifound %d'% (how_many_increments*numb_threads,counter.count))



