import torch

x = torch.randn(3, requires_grad=True) # requires_grad = true because it is false default
# It is required to specify to calculate gradient w.r.t. a variable 'x'
# print(x)

# y = x + 2 # pytorch creates computational graph for it
# # computation graph is used for backpropagation
# z = y*y*2
# # z = z.mean()
# print(z)

# v = torch.tensor([0.1, 1.0, 0.001], dtype=torch.float32) #because it is vector multiplication
# z.backward(v) # dz/dx
# print(x.grad)

# #methods to stop pytorch from creating gradient function
# #m1
# x.requires_grad_(False)
# print(X)
# #m2 
# y = x.detach()
# print(y)
# #m3
# with torch.no_grad():
#     y = x + 2
#     print(y)


#dummy data
weights  =torch.ones(4, requires_grad=True)

for epoch in range(5):
    model_output = (weights*3).sum()

    model_output.backward()

    print(weights.grad)

    weights.grad.zero_()

# optimizer = torch.optim.SGD([weights], lr=0.01)
# optimizer.step()
# optimizer.zero_grad()