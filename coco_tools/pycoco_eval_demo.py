import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
import pylab

pylab.rcParams['figure.figsize'] = (10.0, 8.0)

annType = ['segm', 'bbox', 'keypoints']
annType = annType[1]  # specify type here
prefix = 'person_keypoints' if annType == 'keypoints' else 'instances'
print('Running demo for *%s* results.' % (annType))

# initialize COCO ground truth api
dataType = 'val2017'
annFile = '/home/charan/Documents/research/deep_lite/current_work/annotations_trainval2017/annotations/%s_%s.json' % (prefix, dataType)
cocoGt = COCO(annFile)

# initialize COCO detections api
# resFile = '%s/results/%s_%s_fake%s100_results.json'
# resFile = resFile % (dataDir, prefix, dataType, annType)
cocoDt = cocoGt.loadRes('output.json')

imgIds = sorted(cocoGt.getImgIds())
#imgIds = imgIds[0:100]
#imgId = imgIds[np.random.randint(100)]

# running evaluation
cocoEval = COCOeval(cocoGt, cocoDt, annType)
cocoEval.params.imgIds = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()
