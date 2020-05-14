import torch.nn as nn
import torch.optim as optim
import numpy as np
import torch


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Linear(5, 3),
            nn.ReLU()
        )
        self.layer2 = nn.Sequential(
            nn.Linear(3, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        return x


model = NeuralNetwork()
# Specify the Loss function
criterion = nn.MSELoss()
# Specify the optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

print(model)
data = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
labels = [0, 1, 0, 1, 0]

x_data = np.array(data, dtype=np.float32)
x_data = torch.from_numpy(x_data.reshape(-1, 5)).requires_grad_()

y_data = np.array(labels, dtype=np.float32)
y_data = torch.from_numpy(y_data.reshape(-1, 1))
epochs = 30

train_loss = 0.0
model.train()
for epoch in range(epochs):
    # clear the gradients of all optimized variables
    optimizer.zero_grad()
    # forward pass: compute predicted outputs by passing inputs to the model
    output = model(x_data)
    # calculate the batch loss
    loss = criterion(output, y_data)
    # backward pass: compute gradient of the loss with respect to model parameters
    loss.backward()
    # perform a single optimization step (parameter update)
    optimizer.step()
    print('epoch {}, loss {}'.format(epoch, loss.item()))

x_valid_data = [[1, 1, 1, 1, 1], [3, 3, 3, 3, 3]]
x_valid_data = np.array(x_valid_data, dtype=np.float32)
x_valid_data = torch.from_numpy(x_valid_data)
model.eval()
print(model(x_valid_data))
