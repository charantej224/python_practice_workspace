from python_practice_workspace.pytorch_train.custom_dataset import CustomDataset
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

for images, label in data_loader:
    print(label)