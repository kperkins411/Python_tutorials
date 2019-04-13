import torch

# # target output size of 5x7
# m = torch.nn.AdaptiveMaxPool2d((5, 7))
# input = torch.randn(1, 64, 8, 99)
# output = m(input)
#
#  # target output size of 7x7 (square)
# m = torch.nn.AdaptiveMaxPool2d(7)
# input = torch.randn(1, 64, 10, 9)
# output = m(input)
#
#  # target output size of 10x7
# m = torch.nn.AdaptiveMaxPool2d((None, 7))
# input = torch.randn(1, 64, 10, 9)
# output = m(input)
#
#
#  # target output size of 10x7
# m = torch.nn.AdaptiveMaxPool2d((3,5))
# input = torch.randn(1,10, 9)
# output = m(input)
#
#
# x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# y = x.narrow(0, 0, 2)


input = torch.ones(18).reshape(2,3,3)
input[1,:,:].fill_(2)
input[0,1,1]=3
input[1,1,1]=6

# m = torch.nn.AdaptiveMaxPool2d((2, 2))
m = torch.nn.AdaptiveMaxPool2d((1,1))
output = m(input)

# input = torch.arange(0.0,18.0,1.0).reshape(2,3,3)
input = torch.arange(0.0,75.0,1.0).reshape(3,5,5)

output = m(input)

#make a copy
z=input.narrow(0,1,1)*2
input = torch.narrow(input, 0,1,1)*2

# target output size of 5
m = torch.nn.AdaptiveAvgPool1d(5)
input = torch.randn(1, 64, 8)
output = m(input)
pass