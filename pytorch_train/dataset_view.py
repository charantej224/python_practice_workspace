from pytorch_train.custom_dataset import CustomDataset
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import torch

custom_dataset = CustomDataset(
    root_dir='/home/charan/Documents/workspaces/python_workspaces/python_practice_workspace/pytorch_train/images',
    csv_file='/home/charan/Documents/workspaces/python_workspaces/python_practice_workspace/pytorch_train/image.csv')

batch_size = 1
num_workers = 1

data_loader = torch.utils.data.DataLoader(custom_dataset,
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
