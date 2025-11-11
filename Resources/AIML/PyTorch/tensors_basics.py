import torch
import numpy as np

##simple operations
# x = torch.rand(2, 2)
# y = torch.rand(2, 2)
# print(x)
# print(y)
# y.add_(x)
# print(y)

# #slicing
# x = torch.rand(5, 3)
# print(x)
# print(x[0, :])

# #torch to numpy:   (it can only be done on cpu)
# a = torch.ones(5)
# print(a)
# b = a.numpy()
# print(b)

# a.add_(1) #on cpu if you change 'a' then 'b' also changes
# print(a)
# print(b)

# #numpy to torch
# a = np.ones(5)
# print(a)
# b = torch.from_numpy(a)
# print(b)

# a += 1
# print(a)
# print(b)

x = torch.ones(5, requires_grad=True) #it tell to calculate gradient
print(x)