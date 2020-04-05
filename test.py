import numpy as np
from fastai.basics import *

w=torch.ones(3,3)
w[:,1]+=1

import matplotlib.pyplot as plt
import torch
n=100
x=torch.ones(n,2)
x[:,0].uniform_(-1,1)

# a=np.array([3.,2.])
a=torch.Tensor([3.,2.])
y=x@a
z= torch.rand(n)
# z= torch.rand(n).unsqueeze(0)
y1 = torch.add(y,z)

y =y + torch.rand(n)

import matplotlib.pyplot as plt
# plt.subplot(111)
plt.scatter(x[:,0].numpy(),y.numpy())
plt.show()

#
# xyc = range(20)
#
#
# plt.subplot(121)
#
# # plt.scatter(xyc[:13], xyc[:13], c=xyc[:13], s=35, vmin=0, vmax=20)
# plt.colorbar()
# plt.xlim(0, 20)
# plt.ylim(0, 20)
#
#
# plt.subplot(122)
# plt.scatter(xyc[8:20], xyc[8:20], c=xyc[8:20], s=35, vmin=0, vmax=20)
# plt.colorbar()
# plt.xlim(0, 20)
# plt.ylim(0, 20)
#
#
# plt.show()





x= list('A peachy keen')
record =('acme',10,123.5,(12,18,2012))
name,*_,tup1 = record
*_,year = tup1

numb_iterations = 10
step_size = numb_iterations

max_lr=1
min_lr=.1

first = np.linspace(min_lr, max_lr,step_size)
second = np.linspace(min_lr, first[step_size-2], step_size) #note range to second from end
# second = np.flip(second)

ls = np.concatenate((first,np.flip(second)))



# data = []
# for itr in range(numb_iterations):
#     cycle = math.floor(1 + itr / (2 * step_size))
#     x = abs(itr / step_size - 2 * cycle + 1)
#     lr = min_lr + (max_lr - min_lr) * max(0, (1 - x))
#     data.append(lr)
pass
