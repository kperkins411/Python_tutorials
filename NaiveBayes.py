import numpy as np
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

data = np.arange(28).reshape(4,7)

data1 = data[:,names=='Bob']

data2 = data[3]


#lets use boolean indexing to set all values in dataset to zero
# data3 = (np.random.randn(28).reshape(4,7))[data3<0]=0  #does not work
data3 = np.random.randn(28).reshape(4,7)
data3[data3 < 0] = 0

#filter rows
arr = np.empty((8, 4))

for i in range(8):
    arr[i] = i

b = arr[[4, 3, 0, 6]]
c= arr[ 2,3]
d= arr[[2,3]]
#create dataset
x=np.arange(6).reshape(2,3)
l=x[0]
l1=x[0][:]
l3=x[0][:][0]

z=(x<5)
q=x*z
y=np.array([lambda x:False if x<.5 else True for x in x])
print (x)
print (y)
# y=x[True: x>.5 else False]
# y=np.zeros((4,3), dtype=bool).map(lambda q: True if q>.5 else False,x)
# z = y[x>.5]



def pr(y_i):
    p = x[y==y_i].sum(0)
    return (p+1) / ((y==y_i).sum()+1)