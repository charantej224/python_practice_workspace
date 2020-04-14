from custom_obj_detection.custom_dataset import CustomDataSet
from torch.utils.data import DataLoader
from custom_obj_detection.model_handler import get_model_object_detection
import torch
import torchvision.transforms as T
import sys

transforms = T.Compose([T.Resize(256),
                        T.CenterCrop(224),
                        T.ToTensor(),
                        T.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])])

if sys.argv[1] is not None:
    root_dir = sys.argv[1]
else:
    root_dir = '/home/charan/Documents/workspaces/aeroplane/aeroplane/Datasets/VOC2007/'

print(root_dir)


# collate_fn needs for batch
def collate_fn(batch):
    return tuple(zip(*batch))


train_dataset = CustomDataSet(root_dir=root_dir, classes=['aeroplane'], is_train=True, transforms=transforms)
test_dataset = CustomDataSet(root_dir=root_dir, classes=['aeroplane'], is_train=False, transforms=transforms)

data_loader = DataLoader(train_dataset, batch_size=1, shuffle=False, num_workers=1, collate_fn=collate_fn)
test_data_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, num_workers=1, collate_fn=collate_fn)

# 2 classes; Only target class or background
num_classes = 2
num_epochs = 10
model = get_model_object_detection(num_classes)

# move model to the right device

# parameters
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005, momentum=0.9, weight_decay=0.0005)

len_dataloader = len(data_loader)

for epoch in range(num_epochs):
    model.train()
    i = 0
    for images, annotations in data_loader:
        i += 1
        imgs = list(img for img in images)

        model_inputs = [{k: v for k, v in t.items()} for t in annotations]
        loss_dict = model(imgs, model_inputs)
        losses = sum(loss for loss in loss_dict.values())

        optimizer.zero_grad()
        losses.backward()
        optimizer.step()

        print(f'Iteration: {i}/{len_dataloader}, Loss: {losses}')

model.eval()

for images, annotations in test_data_loader:
    test_dict = model(images)
    print(test_dict)
