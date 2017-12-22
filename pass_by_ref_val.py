
def fun(x):
    x=3
#integers are imutable
a=2
fun(a)

def fun1(x):
    x="toast"
#strings are imutable
a="gg"
fun1(a)

class myc(object):
    def __init__(self):
        self.a=4

def fun2(x):
    x.a=5
#objects are not imutable
b=myc()
fun2(b)
pass
