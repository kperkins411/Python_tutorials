import numpy as np

def get_lrg(b):
    if not b: raise Exception()
    b = sorted(b, key=lambda x: np.product(x[0][-2:] - x[0][:2]), reverse=True)
    return b[0]


x = (np.array([96,155,269,350]),7)

y = np.product(x[0][-2:] - x[0][:2])

y1=np.product([1,2,3,4])

y2=np.product([2,3,4,5])

x=list(x)
x.append(np.array((np.array([229,8,499,244]),7)))

larg = get_lrg(x)