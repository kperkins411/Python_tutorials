from threading import Thread,Lock,Condition
from time import sleep
from threading import Event

class Counter(object):
    def __init__(self):
        self._count=0

    def inc(self,offset):
        self._count += offset

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self,count):
        self._count=count

class Worker(Thread):
    global bDoWork
    global cv

    def __init__(self,func, args):
        super().__init__()
        self.func=func
        self.args = args
        self.polled_count=0
        self.work_done =0

    def run(self):
        # self.func(self.args[0], self.args[1])
        self.func(**self.args)

        # while bDoWork:
        #     self.event_1.wait()  # wait for notice
        #     print('thread %s notified' % self.args[0])
        #     sleep(0.001)
        #     self.event_1.clear()


event1 = Event()
event2 = Event()
cnt = Counter()
cv = Condition()


# Example 1
def consume(id, evt,lck):
    print('enter thread %s consume' % (id))
    global cnt
    global bDoWork
    global cv

    while (True):

        with cv:
            if cnt.count == 0 and iNumbProducers == 0:
                break
            elif cnt.count == 0:
                cv.wait()
            else:
                cnt.inc(-1)
                print('thread %s consumeing, cnt is %d' % (id,cnt.count ))
            # cnt.count  =cnt.count - 1
            # with lck:
            #     cnt-=1

    with cv:
        print('thread %s consume, EXITING' % (id))
    return

total_incs=100000
iNumbProducers = 6
lck = Lock()
def produce(id, evt,lck):
    print('enter thread %s produce' % (id))
    global cnt
    global iNumbProducers
    global cv

    cntdown = total_incs
    while (cntdown > 0):
        with cv:
            cnt.inc(1)

            # cnt.count =cnt.count + 1
            # with lck:
            #     cnt+=1;
            if (cntdown%20==0):
                print("         cnt is %d"%cnt.count)
            cntdown-=1;
            cv.notifyAll()
        # print('thread %s produce' % (id))

    with cv:
        print('thread %s produce, EXITING' % (id))
        iNumbProducers-=1
        cv.notifyAll()
    return

threads = [ Worker(consume,args =dict(id=1,evt=event1,lck =lck)),
            Worker(consume,args =dict(id=2,evt=event1,lck =lck)),
            Worker(consume,args =dict(id=3,evt=event1,lck =lck)),
            Worker(consume,args =dict(id=4,evt=event1,lck =lck)),
            Worker(consume,args =dict(id=5,evt=event1,lck =lck)),

            Worker(produce,args=dict(id=6,evt=event1,lck =lck)),
            Worker(produce,args=dict(id=7,evt=event1,lck =lck)),
            Worker(produce,args=dict(id=8,evt=event1,lck =lck)),
            Worker(produce,args=dict(id=10,evt=event1,lck =lck)),
            Worker(produce,args=dict(id=11,evt=event1,lck =lck)),
            Worker(produce, args=dict(id=12, evt=event1,lck =lck))]

for thread in threads:
    thread.start()


# sleep(0.1)


# Stop all the threads by causing an exception in their
# run methods.
for thread in threads:
    thread.join()

print("the count is %d"%cnt.count)

# processed = len(done_queue.items)
# polled = sum(t.polled_count for t in threads)
# print('Processed',processed,' items after polling', polled, ' times')
#


