'''
illustrating stateful closures and callable
'''
from collections import defaultdict

def myfunc(d1,d2):
    a=0

    def check():
        nonlocal a
        a+=1
        return 0

    dc=defaultdict(check,d1)
    for key in d2:
        dc[key]+=d2[key]

    return dc,a

class Tracker():
    def __init__(self):
        self.a = 0

    def default(self):
        self.a += 1
        return 0


class Callable():
    def __init__(self):
        self.a = 0

    def __call__(self, *args, **kwargs):
        self.a += 1
        return 0

def display(s,dc,a):
    print(s)
    for key in dc:
        print(key + ":" + str(dc[key]))
        # print(lambda k, v: k + ':' + str(v), dc)
    print("new value added " + str(a) + " times\n")


d1 = {"red": 1, "blue": 2}
d2 = {"green": 3, "blue": 17, "orange": 4}


dc,a = myfunc(d1,d2)
display("using stateful closures", dc,a)

myTracker = Tracker()
dc=defaultdict(myTracker.default,d1)
for key in d2:
    dc[key] += d2[key]
display("using plain class", dc,myTracker.a)

myCallable = Callable()
dc=defaultdict(myCallable,d1)
for key in d2:
    dc[key] += d2[key]
display("using callable class", dc,myCallable.a)




