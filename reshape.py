import torch

x= [x for x in range(6)]
y= torch.tensor(x)
z = y.view(2,3)
pass