pad = 1 if 500%11 >0 else 0
x= 100//9
# self.numb_images/self.batch_size)*multiplier + pad

y=[0,1,2]
z=len(y)

if max_lr_reducer is None:
    max_lr_reducer =1

myd= {}
name = myd.setdefault('name','keith')
name1 = myd['name']
keys = myd.keys()

from threading import Lock
lock = Lock()

lock.acquire(True) # will block if lock is already held
# ... access shared resource
lock.release()