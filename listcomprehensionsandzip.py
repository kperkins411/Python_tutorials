a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
y=list(x)   #list of tuples
z=[[x1[0],x1[1]] for x1 in zip(a,b) ]
#use the tuple() function to display a readable version of the result:
y=tuple(x)[0]
print(tuple(x))

def show(*args):
    for a in args:
        print(a)

names = ['keith', 'allen','lynn']

show(names)
show(*names)

print(names)
print(*names)
# a=list(*names)
b={x:y for x,y in enumerate(names)}

b=[[0,1,2],[3,4,5],[6,7,8]]

b_t =[x for x in zip(b)]
b_t1 =[list(x) for x in zip(*b)]


names_len = [len(k) for k in names]
sn=names_len[0]
for i,j in enumerate(names):
    if names_len[i]<sn:
        sn=i
print(f"shortest name is {names[sn]}")

#a faster way
sl=names_len[0]
sn=names[0]
for i,j in zip(names,names_len):
    if j<sl:
        sn=i
print(f"shortest name is {sn}")




l1=[1,2,3]
l2=[4,5,6]
g1=((x,y) for x,y in zip(l1,l2))
l4=list(g1)

#now flatten the list of tuples
g1=((x,y) for x,y in zip(l1,l2))
l3=[item for tup in g1 for item in tup]

g1=((x,y) for x,y in zip(l1,l2))
for tup in g1:
    print(str(tup))

def transpose_list(list_of_lists):
    return [
        list(row)
        for row in zip(*list_of_lists)
    ]

list_of_lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
c=list(zip(*list_of_lists))

transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


c=range(5)
a=[x for x in range(10)]
b=list((x for x in range(10)))
class Numbs:
    def __init__(self,*args):
        self.args = args
    def __add__(self, other):
        return Numbs( *(x+y for x,y in zip(self.args,other.args)))
a=Numbs(1,2,3)
b=Numbs(4,5,6)
c=a+b
