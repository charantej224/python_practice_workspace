from torch.utils.data import Dataset
import os
from PIL import Image
import xml.etree.ElementTree as ET
import torch


class CustomDataSet(Dataset):

    def __init__(self, root_dir, classes=[], is_train=True, transforms=None):
        self.root_dir = root_dir
        self.annotations_path = os.path.join(root_dir, 'Annotations')
        self.images_path = os.path.join(root_dir, 'JPEGImages')
        if is_train:
            self.image_sets = open(os.path.join(root_dir, 'ImageSets/Main/train.txt'), 'r')
        else:
            self.image_sets = open(os.path.join(root_dir, 'ImageSets/Main/validation.txt'), 'r')
        self.ids = sorted([each_value.strip() for each_value in self.image_sets.readlines()])
        self.image_sets.close()
        self.classes = classes
        self.transforms = transforms

    def __getitem__(self, index):
        image_id = self.ids[index] + '.jpg'
        image = Image.open(os.path.join(self.images_path, image_id))
        if self.transforms is not None:
            image = self.transforms(image)
        xml_file = self.ids[index] + '.xml'
        annotations = ET.parse(os.path.join(self.annotations_path, xml_file))
        root = annotations.getroot()
        boxes = []
        labels = []
        is_crowd = []
        for each_object in root.iter('object'):
            xmin = float(each_object.find('bndbox/xmin').text)
            ymin = float(each_object.find('bndbox/ymin').text)
            xmax = float(each_object.find('bndbox/xmax').text)
            ymax = float(each_object.find('bndbox/ymax').text)
            label = each_object.find('name').text
            boxes.append([xmin, ymin, xmax, ymax])
            labels.append(self.classes.index(label))
            is_crowd.append(0)

        boxes = torch.as_tensor(boxes, dtype=torch.float32)
        labels = torch.as_tensor(labels, dtype=torch.int64)
        image_id = torch.tensor([index])
        area = (boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0])
        is_crowd = torch.as_tensor(is_crowd, dtype=torch.int64)

        target = {}
        target["boxes"] = boxes
        target["labels"] = labels
        # target["masks"] = masks
        target["image_id"] = image_id
        target["area"] = area
        target["iscrowd"] = is_crowd

        return image, target

    def __len__(self):
        return len(self.ids)
