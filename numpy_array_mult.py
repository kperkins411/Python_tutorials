import numpy as np

a = np.array([[1, 0], [0, 1]])
b = np.array([1, 2])
c= np.matmul(a, b)

#matrix multiply
d= np.matmul(b,a)

x= np.array(range(12)).reshape(3,4)
w= np.array(range(4)).reshape(1,4)
# element by element multiply
z=w*x

z1=np.dot(w,x.T)

q= np.matmul(w,x.T)
pass