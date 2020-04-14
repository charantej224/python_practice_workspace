from pytorch_train.simple_dataset import simpleDataset
import torch
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

root = "/home/charan/Documents/workspaces/python_workspaces/python_practice_workspace/pytorch_train/images/"

# assume we have 3 jpg images
filenames = ['Image1.png', 'Image2.png', 'Image3.png', 'Image4.png', 'Image5.png', 'Image6.png', 'Image7.png',
             'Image8.png']

# the class of image might be ['black cat', 'tabby cat', 'tabby cat']
labels = [0, 1, 1, 0, 1, 1, 0, 1]

# create own Dataset
my_dataset = simpleDataset(root=root,
                           filenames=filenames,
                           labels=labels
                           )

# data loader
batch_size = 1
num_workers = 4

data_loader = torch.utils.data.DataLoader(my_dataset,
                                          batch_size=batch_size,
                                          shuffle=False,
                                          num_workers=num_workers
                                          )

for images, labels in data_loader:
    # image shape is [batch_size, 3 (due to RGB), height, width]
    img = transforms.ToPILImage()(images[0])
    plt.imshow(img)
    plt.show()
    print(labels)
