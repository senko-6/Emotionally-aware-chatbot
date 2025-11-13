import torch

x = torch.tensor(1.0)
y = torch.tensor(2.0)

w = torch.tensor(1.0, requires_grad = True)
b = torch.tensor(1.0, requires_grad = True)

# forward pass and compute the loss:
y_hat = w * x + b
loss = -(y*torch.log(y_hat) + (1-y)*torch.log(1-y_hat))

print(loss)

# backward pass:
loss.backward()
print(w.grad)

