import numpy as np
import timeit
import itertools

list_a = [1, 2, 4, 6]*10000
fil = [True, False, True, False]*10000
list_a_np = np.array(list_a)
fil_np = np.array(fil)

lst=list_a_np[fil_np]

nmb=1000
tme = timeit.timeit( 'list(itertools.compress([1, 2, 4, 6]*10000, [True, False, True, False]*10000))', number=nmb)
print (tme/1000)

# tme = timeit.timeit( 'import numpy; itertools.compress(numpy.tile(numpy.array([1, 2, 4, 6]),1000), numpy.tile(numpy.array([True, False, True, False]),1000)))', number=nmb)
print (tme/1000)

colors = ["Goldenrod", "purple", "Salmon", "turquoise", "cyan"]
b= sorted(colors, key=lambda s: s.casefold())


colors = ["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"]

def normalize_case(string):
    return string.casefold()

normalized_colors = list(map(normalize_case, colors))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(myfunc(2)(11))
print(mydoubler(11))

d1 = {"red": 1, "blue": 2}
d2 = {"green": 3, "blue": 17, "orange": 4}

d3=[("green", 3),( "blue", 17),( "orange", 4)]
d4=[1, 5, 4, 6, 8, 11, 3, 12]
l2=list(d2)
print("test1")
# map(lambda x: print("test"), d4)
# map(lambda x: print( "("+x[0]+":"+x[1]+ ")"), d3)
pass

xx=[1,2,3,4,5,-6,7,-8]
# xxx = xx.reshape(2,2,2)
yy=list(filter(lambda x: x if x%2==0 else None,xx))
y=list(filter(lambda x: (x%2==0), xx))
zz= list(map(lambda x:0 if x<0 else x,xx))

z1= list(map(lambda x: x<0,xx))
z2=xx[z1]
print (y)
pass