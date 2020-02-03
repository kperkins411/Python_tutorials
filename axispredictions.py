import  numpy as np
def mult1(a,b):
    return a*b


a = np.array([1,2,3,4])
aa = [1,2,3,4]
b = 3*a
bb = 3*aa
print (b)
print(bb)

c=  a*3
d = mult1(a,3)

class mult():
    def __init__(self,i):
        self.mult = i

    def trans(self, x):
        res = x*self.mult
        return res

m3 = mult(3)
e = m3.trans(a)

# create a list of these multipliers
mults = [mult(i) for i in range(10)]

# create some data
vals=range(5)

# what is this weirdness it duplicates vals 3 times!
f = 3*vals

results = [m.trans(a) for m in mults]

results1=[]
for val in vals:
    results1 = [m.trans(val) for m in mults]
    print(results1)


matrix=[[[1,2,3],[4,5,6],[7,8,9]],[[10,20,30],[40,50,60],[70,80,90]]]

m1 = mult(3)
# [m55.trans(x) for m in matrix for row in m for x in row]
average = np.mean( [m1.trans(row) for m in matrix for row in m ], axis=0)

average = np.mean( [m1.trans(np.asarray(row)) for m in matrix for row in m ], axis=0)

print average

# flat = [x+100 for m in matrix for r in m for x in r]
# print (flat)
# flat1 = [x for x in row for row in matrix]
# print (flat1)