import torch.nn as nn
import torch.optim as optim
import numpy as np
import torch


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(5, 3)
        self.layer2 = nn.Linear(3, 1)
        self.sig = nn.Sigmoid()

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.sig(x)


model = NeuralNetwork()
# Specify the Loss function
criterion = nn.CrossEntropyLoss()
# Specify the optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

print(model)
data = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
labels = [0, 1, 0, 1, 0]

epochs = 5

train_loss = 0.0
model.train()
for epoch in range(epochs):

    for i in range(len(data)):
        print(np.array(data[i]).shape)
        val = torch.from_numpy(np.array(data[i]))

        # clear the gradients of all optimized variables
        optimizer.zero_grad()
        # forward pass: compute predicted outputs by passing inputs to the model
        output = model(val)
        # calculate the batch loss
        loss = criterion(output, labels[i])
        # backward pass: compute gradient of the loss with respect to model parameters
        loss.backward()
        # perform a single optimization step (parameter update)
        optimizer.step()
        # update training loss
        train_loss += loss.item() * data.size(0)
