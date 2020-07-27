from pycocotools.coco import COCO

annType = ['segm', 'bbox', 'keypoints']
annType = annType[1]  # specify type here
prefix = 'person_keypoints' if annType == 'keypoints' else 'instances'

dataType = 'val2017'
annFile = '/home/charan/Documents/research/deep_lite/current_work/annotations_trainval2017/annotations/%s_%s.json' % (
    prefix, dataType)
# cocoGt = COCO(annFile)
# ann = cocoGt.loadImgs([289343])
# print(ann)
# print(ann[0]['width'])
# print(ann[0]['height'])

import json

with open(annFile, 'r') as f:
    annotation_dict = json.load(f)
    f.close()

categories_list = annotation_dict["categories"]

index_list = []
list_of_lists = []

for each in categories_list:
    if each['supercategory'] not in index_list:
        index_list.append(each['supercategory'])
        cat_list = []
        list_of_lists.append(cat_list)
    index_val = index_list.index(each['supercategory'])
    list_of_lists[index_val].append(each['name'])

for counter in range(len(index_list)):
    string_val = " - ".join(list_of_lists[counter])
    print(index_list[counter] + " === " + string_val)

with open("semantic_context.txt","w") as f:
    f.write(str(list_of_lists))
    f.close()
