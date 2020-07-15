from pycocotools.coco import COCO

annType = ['segm', 'bbox', 'keypoints']
annType = annType[1]  # specify type here
prefix = 'person_keypoints' if annType == 'keypoints' else 'instances'

dataType = 'val2017'
annFile = '/home/charan/Documents/research/deep_lite/current_work/annotations_trainval2017/annotations/%s_%s.json' % (
    prefix, dataType)
cocoGt = COCO(annFile)
ann = cocoGt.loadImgs([289343])
print(ann)
print(ann[0]['width'])
print(ann[0]['height'])
