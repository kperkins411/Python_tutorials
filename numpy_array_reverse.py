
# shallow verses deep copy of numpy arrays
import numpy as np

x = np.ones([30])

#make a shallow copy of x
y=x.reshape(3,10)
y=y.reshape(30)

#make a deep copy of x
z=np.copy(x)

assert x.all()==y.all() # and x is not y will return true
y[3]=22
z[3]=66
pass