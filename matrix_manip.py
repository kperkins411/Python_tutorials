import numpy as np

N = 10
a = np.random.rand(N,N)
b = np.zeros((N,N+1))
b[:,:-1] = a


N = 3
A = np.eye(N)

A= np.c_[ A, np.ones(N) ]


b = np.hstack((a, np.zeros((a.shape[0], 1), dtype=a.dtype)))

a = np.arange(2*4).reshape((2,4))
b = np.arange(2*4).reshape((4,2))
c= np.matmul(a,b).shape
d = np.transpose(a)
pass
# -----
# w = np.array([1,2])
# y=np.array([10])
# x_val=np.array([2])
# x=np.vstack((x_val, np.ones((x_val.shape[0]), dtype=x_val.dtype)))
# # z= w*x
# z1=w@x
# z2=np.matmul(w,x)

#-------

x1=np.matrix([3,2])
#
# w = np.matrix([2,1])
# x = np.matrix([x1,3])
#
# y = x[0].shape[1]
#
# y=w*np.transpose(x)
# pass
# z1=w@x
def backprop_vectorize(lr,epochs, w, x, y):
    '''
    backprop over errorfunction to adjust w1 and w2
    :param lr: learning rate
    :param w: weight vector (same size as x, add 1 to end if necessary)
    :param x: values vector dependent
    :param y: results vector independent
    :return:
    '''
    #the first param has all the values, get the number of columns for the number of samples
    numb_samples=len(x[0])
    divisor = 1
    error_last=None
    w_old = w
    for epoch in range(epochs):
        total = 0
        error = np.sum((1/2)*(y-w@x)**2, axis=1)/numb_samples
        if error_last==None:
            error_last=error
        print(f"Error is {error}")

        if error>error_last:
            w=w_old
            lr=lr/2
            print(f"lr is now {lr}")

        # sum de/dw1 and de/dw2
        total = np.sum(-(y - w @ x) * x, axis=0)

        # divide by numb_samples
        grad_w = total / numb_samples

        # adjust w1 and w2
        w_old = w
        w = w - np.transpose(lr * grad_w)

        error_last = error
    return w
#y=3x+4
#y=w1x1 + w2*1
# w = np.matrix([.3,.2])
# y=np.matrix([10,13])
#
# x_val=np.matrix([2,3])
# x=np.matrix([x_val,1])

# Gen up some dummy data
w = np.array([[1.0,2.0]])

# y=np.array([10,13])
y=np.array([10.0,13])

#all the possible X values
# x_val=np.array([2,3])
x_val=np.array([2.0,3])

# x=np.array([x_val,1])
x=np.vstack((x_val, np.ones((x_val.shape[0]), dtype=x_val.dtype)))
# b = np.hstack((a, np.zeros((a.shape[0], 1), dtype=a.dtype)))

w=backprop_vectorize(.01,1000, w, x, y)
print(f"for X {x} and y{y} weights are {w} ")
