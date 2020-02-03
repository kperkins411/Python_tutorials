from threading import Thread,Lock
from collections import deque
from queue import Queue

class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    # Example 18
    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return  # Cause the thread to exit
                yield item
            finally:
                self.task_done()


class myQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock=Lock()

    def put(self,item):
        # with self.lock:
        self.items.append(item)

    def get(self):
        # with self.lock:
        return self.items.popleft()

from time import sleep
from threading import Event
class Worker(Thread):
    def __init__(self,func, in_queue,in_queue_event, out_queue,out_queue_event):
        super().__init__()
        self.func=func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.in_queue_event = in_queue_event
        self.out_queue_event = out_queue_event
        self.polled_count=0
        self.work_done =0

    def run(self):
        global bDone
        while True:

            self.polled_count+=1
            try:
                self.in_queue_event.wait()  # wait for notice
                item=self.in_queue.get()
            except IndexError:
                self.in_queue_event.clear()
                if bDone == True:
                    return
                sleep(0.01)
            else:
                result=self.func(item)
                self.out_queue.put(result)
                self.out_queue_event.set()

bDone = False
download_queue = myQueue()
download_queue_event = Event()

resize_queue = myQueue()
resize_queue_event = Event()

upload_queue = myQueue()
upload_queue_event = Event()

done_queue = myQueue()
done_queue_event = Event()


# Example 1
def download(item):
    return item

def resize(item):
    return item

def upload(item):
    return item


threads = [Worker(download,download_queue,download_queue_event, resize_queue,resize_queue_event),
           Worker(resize,resize_queue,resize_queue_event, upload_queue,upload_queue_event ),
           Worker(upload,upload_queue,upload_queue_event,done_queue,done_queue_event)]

for thread in threads:
    thread.start()

for _ in range(1000):
    download_queue.put(object())

download_queue_event.set()

import time
while(len(done_queue.items)<100):
    time.sleep(0.1)

# Stop all the threads by causing an exception in their
# run methods.
for thread in threads:
    thread.in_queue = None

processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print('Processed',processed,' items after polling', polled, ' times')



