import os
from torch.utils.data import Dataset
import pandas as pd
import torchvision.transforms as transforms
from PIL import Image
import torch


class CustomDataset(Dataset):
    def __init__(self, root_dir, csv_file):
        self.root_dir = root_dir
        self.csv_file = pd.read_csv(csv_file)

    def __getitem__(self, item):
        print()
        label = self.csv_file[item]
        image = Image.open(os.path.join(self.root_dir, label))

        # output of Dataset must be tensor
        image = transforms.ToTensor()(image)
        label = torch.as_tensor(label, dtype=torch.int64)
        return image, label

    def __len__(self):
        return len(self.csv_file)
