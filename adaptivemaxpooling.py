import torch

'''
The other name for it is “global pooling”, although they are not 100% the same. With global avg/max pooling the
size of the resulting feature map is 1x1xchannels. With adaptive pooling, you can reduce it to any feature map size
you want, although in practice we often choose size 1, in which case it does the same thing as global pooling.

What happens is exactly the same as with regular average or max pooling, but instead of specifying the size of the
pooling window (e.g. 2x2) you specify the size of the output feature map that you want (and the size of the pooling
window is automatically computed from that).
'''

x = torch.randn(1, 1, 7, 7)

m1 = torch.nn.AvgPool2d(kernel_size=7, stride=7, padding=0)
# i1 = torch.Variable(x)
o1 = m1(x)
print(o1.shape)

m2 = torch.nn.AdaptiveAvgPool2d(1)
o2 = m2(x)
o2.shape
pass


