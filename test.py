myd= {}
name = myd.setdefault('name','keith')
name1 = myd['name']
keys = myd.keys()

from threading import Lock
lock = Lock()

lock.acquire(True) # will block if lock is already held
# ... access shared resource
lock.release()