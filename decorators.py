import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(3)

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print ('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts))
        return result

    return timed

class Foo(object):

    @timeit
    def foo(self, a=2, b=3):
        time.sleep(0.2)

@timeit
def f1():
    time.sleep(.3)
    # print ('f1')

@timeit
def f2(a):
    time.sleep(.4)
    # print ('f2',a)

@timeit
def f3(a, *args, **kw):
    time.sleep(0.3)
    # print ('f3', args, kw)

f1()
f2(42)
f3(42, 43, foo=2)
Foo().foo()