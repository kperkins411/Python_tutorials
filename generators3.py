def multigen(gen_func):
    class _multigen(object):
        def __init__(self, *args, **kwargs):
            self.__args = args
            self.__kwargs = kwargs
            self.num_epochs =3
        def __iter__(self):
            self.num_epochs-=1
            if (self.num_epochs>=0):
                return gen_func(*self.__args, **self.__kwargs)
            else:
                raise StopIteration
    return _multigen

@multigen
def myxrange(n):
   i = 0
   while i < n:
     yield i
     i += 1
m = myxrange(5)
print (list(m))
print (list(m))
print (list(m))
print (list(m))
#
# a=[0,1,2,3,4,5]
#
# for x in y:
#     print(x)