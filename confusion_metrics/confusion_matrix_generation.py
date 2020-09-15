from pycocotools.coco import COCO
import json
from tqdm.notebook import tqdm
import pandas as pd

import random

import mxnet as mx

"""Visualize image."""

import numpy as np

backbone = "0.001_predictions"
with open(backbone + '/0.001_regular.json') as f:
    preds = json.load(f)
    f.close()
with open(backbone + '/0.001_semantic.json') as f:
    semantic_preds = json.load(f)
    f.close()
with open(backbone + '/0.001_disAnova.json') as f:
    DISANOVA_preds = json.load(f)
    f.close()
with open(backbone + '/0.001_anova.json') as f:
    ANOVA_preds = json.load(f)
    f.close()
with open(backbone + '/0.001_co_occurances.json') as f:
    cooccurrences_preds = json.load(f)
    f.close()

cocoGt = COCO(
    '/home/charan/Documents/research/deep_lite/current_work/annotations_trainval2017/annotations/instances_val2017.json')
with open(
        '/home/charan/Documents/research/deep_lite/current_work/annotations_trainval2017/annotations/instances_val2017.json') as f:
    GTs = json.load(f)
    f.close()

# Load the categories in a variable
catIDs = cocoGt.getCatIds()
cats = cocoGt.loadCats(catIDs)


def getClassName(classID):
    for i in range(len(cats)):
        if cats[i]['id'] == classID:
            return cats[i]['name']
    return "None"


print('The class name is', getClassName(77))

GT_dict = {}
for idx, gt in enumerate(tqdm(GTs['annotations'])):
    image_id = gt['image_id']
    bbox = [gt['bbox'][0], gt['bbox'][1], gt['bbox'][0] + gt['bbox'][2], gt['bbox'][1] + gt['bbox'][3]]
    cls_gt = getClassName(gt['category_id'])  # .replace(" ", "-")
    img = cocoGt.loadImgs([image_id])[0]
    #     I = io.imread(img['coco_url'])
    #     plt.axis('off')
    #     plt.imshow(I)

    if image_id not in GT_dict:
        GT_dict[image_id] = {'bbox': [bbox], 'class_name': [cls_gt]}
    else:
        GT_dict[image_id]['bbox'].append(bbox)
        GT_dict[image_id]['class_name'].append(cls_gt)
#     if idx == 100:
#         break


##### Regular
column_names = ['image_id', 'coco_url', 'class_name', 'bboxes', 'scores', 'gt_class_name', 'gt_bboxes']
regular_df = pd.DataFrame(columns=column_names)
regular_dict = {}
for i, pred in enumerate(tqdm(preds)):
    image_id = pred['image_id']
    score = pred['score']
    bbox = [pred['bbox'][0], pred['bbox'][1], pred['bbox'][0] + pred['bbox'][2], pred['bbox'][1] + pred['bbox'][3]]
    cls_pred = getClassName(pred['category_id'])  # .replace(" ", "-")
    if image_id not in regular_dict:
        regular_dict[image_id] = {'bbox': [bbox], 'class_name': [cls_pred], 'scores': [score]}
    else:
        regular_dict[image_id]['bbox'].append(bbox)
        regular_dict[image_id]['class_name'].append(cls_pred)
        regular_dict[image_id]['scores'].append(score)
#     if i == 100:
#         break

# print(regular_dict)
for image_id, gt in GT_dict.items():
    gt_class_name = gt['class_name']
    gt_bboxes = gt['bbox']
    img = cocoGt.loadImgs([image_id])[0]
    img_url = img['coco_url']

    class_name = []
    bboxes = []
    scores = []
    if image_id in regular_dict:
        bboxes = regular_dict[image_id]['bbox']
        class_name = regular_dict[image_id]['class_name']
        scores = regular_dict[image_id]['scores']

    row_data = [[image_id, img_url, class_name, bboxes, scores, gt_class_name, gt_bboxes]]
    data_df = pd.DataFrame(row_data, columns=column_names)
    regular_df = regular_df.append(data_df, ignore_index=True)

#### semantic
column_names = ['image_id', 'coco_url', 'class_name', 'bboxes', 'scores', 'gt_class_name', 'gt_bboxes']
semantic_df = pd.DataFrame(columns=column_names)
semantic_dict = {}
for i, semantic_pred in enumerate(tqdm(semantic_preds)):
    image_id = semantic_pred['image_id']
    score = semantic_pred['score']
    bbox = [semantic_pred['bbox'][0], semantic_pred['bbox'][1], semantic_pred['bbox'][0] + semantic_pred['bbox'][2],
            semantic_pred['bbox'][1] + semantic_pred['bbox'][3]]
    cls_semantic_pred = getClassName(semantic_pred['category_id'])  # .replace(" ", "-")
    if image_id not in semantic_dict:
        semantic_dict[image_id] = {'bbox': [bbox], 'class_name': [cls_semantic_pred], 'scores': [score]}
    else:
        semantic_dict[image_id]['bbox'].append(bbox)
        semantic_dict[image_id]['class_name'].append(cls_semantic_pred)
        semantic_dict[image_id]['scores'].append(score)
#     if i == 100:
#         break

# semantic_dict
for image_id, gt in GT_dict.items():
    gt_class_name = gt['class_name']
    gt_bboxes = gt['bbox']
    img = cocoGt.loadImgs([image_id])[0]
    img_url = img['coco_url']

    class_name = []
    bboxes = []
    scores = []
    if image_id in semantic_dict:
        bboxes = semantic_dict[image_id]['bbox']
        class_name = semantic_dict[image_id]['class_name']
        scores = semantic_dict[image_id]['scores']

    row_data = [[image_id, img_url, class_name, bboxes, scores, gt_class_name, gt_bboxes]]
    data_df = pd.DataFrame(row_data, columns=column_names)
    semantic_df = semantic_df.append(data_df, ignore_index=True)

### Dis ANova

column_names = ['image_id', 'coco_url', 'class_name', 'bboxes', 'scores', 'gt_class_name', 'gt_bboxes']
DISANOVA_df = pd.DataFrame(columns=column_names)
DISANOVA_dict = {}
for i, DISANOVA_pred in enumerate(tqdm(DISANOVA_preds)):
    image_id = DISANOVA_pred['image_id']
    score = DISANOVA_pred['score']
    bbox = [DISANOVA_pred['bbox'][0], DISANOVA_pred['bbox'][1], DISANOVA_pred['bbox'][0] + DISANOVA_pred['bbox'][2],
            DISANOVA_pred['bbox'][1] + DISANOVA_pred['bbox'][3]]
    cls_DISANOVA_pred = getClassName(DISANOVA_pred['category_id'])  # .replace(" ", "-")
    if image_id not in DISANOVA_dict:
        DISANOVA_dict[image_id] = {'bbox': [bbox], 'class_name': [cls_DISANOVA_pred], 'scores': [score]}
    else:
        DISANOVA_dict[image_id]['bbox'].append(bbox)
        DISANOVA_dict[image_id]['class_name'].append(cls_DISANOVA_pred)
        DISANOVA_dict[image_id]['scores'].append(score)
#     if i == 100:
#         break

# DISANOVA_dict
for image_id, gt in GT_dict.items():
    gt_class_name = gt['class_name']
    gt_bboxes = gt['bbox']
    img = cocoGt.loadImgs([image_id])[0]
    img_url = img['coco_url']

    class_name = []
    bboxes = []
    scores = []
    if image_id in DISANOVA_dict:
        bboxes = DISANOVA_dict[image_id]['bbox']
        class_name = DISANOVA_dict[image_id]['class_name']
        scores = DISANOVA_dict[image_id]['scores']

    row_data = [[image_id, img_url, class_name, bboxes, scores, gt_class_name, gt_bboxes]]
    data_df = pd.DataFrame(row_data, columns=column_names)
    DISANOVA_df = DISANOVA_df.append(data_df, ignore_index=True)

####### Anova

column_names = ['image_id', 'coco_url', 'class_name', 'bboxes', 'scores', 'gt_class_name', 'gt_bboxes']
ANOVA_df = pd.DataFrame(columns=column_names)
ANOVA_dict = {}
for i, ANOVA_pred in enumerate(tqdm(ANOVA_preds)):
    image_id = ANOVA_pred['image_id']
    score = ANOVA_pred['score']
    bbox = [ANOVA_pred['bbox'][0], ANOVA_pred['bbox'][1], ANOVA_pred['bbox'][0] + ANOVA_pred['bbox'][2],
            ANOVA_pred['bbox'][1] + ANOVA_pred['bbox'][3]]
    cls_ANOVA_pred = getClassName(ANOVA_pred['category_id'])  # .replace(" ", "-")
    if image_id not in ANOVA_dict:
        ANOVA_dict[image_id] = {'bbox': [bbox], 'class_name': [cls_ANOVA_pred], 'scores': [score]}
    else:
        ANOVA_dict[image_id]['bbox'].append(bbox)
        ANOVA_dict[image_id]['class_name'].append(cls_ANOVA_pred)
        ANOVA_dict[image_id]['scores'].append(score)
#     if i == 100:
#         break

# ANOVA_dict
for image_id, gt in GT_dict.items():
    gt_class_name = gt['class_name']
    gt_bboxes = gt['bbox']
    img = cocoGt.loadImgs([image_id])[0]
    img_url = img['coco_url']

    class_name = []
    bboxes = []
    scores = []
    if image_id in ANOVA_dict:
        bboxes = ANOVA_dict[image_id]['bbox']
        class_name = ANOVA_dict[image_id]['class_name']
        scores = ANOVA_dict[image_id]['scores']

    row_data = [[image_id, img_url, class_name, bboxes, scores, gt_class_name, gt_bboxes]]
    data_df = pd.DataFrame(row_data, columns=column_names)
    ANOVA_df = ANOVA_df.append(data_df, ignore_index=True)

#### co-occurance
column_names = ['image_id', 'coco_url', 'class_name', 'bboxes', 'scores', 'gt_class_name', 'gt_bboxes']
cooccurrences_df = pd.DataFrame(columns=column_names)
cooccurrences_dict = {}
for i, cooccurrences_pred in enumerate(tqdm(cooccurrences_preds)):
    image_id = cooccurrences_pred['image_id']
    score = cooccurrences_pred['score']
    bbox = [cooccurrences_pred['bbox'][0], cooccurrences_pred['bbox'][1],
            cooccurrences_pred['bbox'][0] + cooccurrences_pred['bbox'][2],
            cooccurrences_pred['bbox'][1] + cooccurrences_pred['bbox'][3]]
    cls_cooccurrences_pred = getClassName(cooccurrences_pred['category_id'])  # .replace(" ", "-")
    if image_id not in cooccurrences_dict:
        cooccurrences_dict[image_id] = {'bbox': [bbox], 'class_name': [cls_cooccurrences_pred], 'scores': [score]}
    else:
        cooccurrences_dict[image_id]['bbox'].append(bbox)
        cooccurrences_dict[image_id]['class_name'].append(cls_cooccurrences_pred)
        cooccurrences_dict[image_id]['scores'].append(score)
#     if i == 100:
#         break

# cooccurrences_dict
for image_id, gt in GT_dict.items():
    gt_class_name = gt['class_name']
    gt_bboxes = gt['bbox']
    img = cocoGt.loadImgs([image_id])[0]
    img_url = img['coco_url']

    class_name = []
    bboxes = []
    scores = []
    if image_id in cooccurrences_dict:
        bboxes = cooccurrences_dict[image_id]['bbox']
        class_name = cooccurrences_dict[image_id]['class_name']
        scores = cooccurrences_dict[image_id]['scores']

    row_data = [[image_id, img_url, class_name, bboxes, scores, gt_class_name, gt_bboxes]]
    data_df = pd.DataFrame(row_data, columns=column_names)
    cooccurrences_df = cooccurrences_df.append(data_df, ignore_index=True)

df_list = [regular_df, ANOVA_df, DISANOVA_df, cooccurrences_df, semantic_df]
label_list = ['REGULAR', 'ANOVA', 'DISANOVA', 'COOCCURRENCES', 'SEMANTIC-CATEGORICAL GROUPING']

"""Bounding box visualization functions."""


def plot_image(img, ax=None, reverse_rgb=False):
    """Visualize image.

    Parameters
    ----------
    img : numpy.ndarray or mxnet.nd.NDArray
        Image with shape `H, W, 3`.
    ax : matplotlib axes, optional
        You can reuse previous axes if provided.
    reverse_rgb : bool, optional
        Reverse RGB<->BGR orders if `True`.

    Returns
    -------
    matplotlib axes
        The ploted axes.

    Examples
    --------

    from matplotlib import pyplot as plt
    ax = plot_image(img)
    plt.show()
    """
    from matplotlib import pyplot as plt
    if ax is None:
        # create new axes
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
    if isinstance(img, mx.nd.NDArray):
        img = img.asnumpy()
    img = img.copy()
    if reverse_rgb:
        img[:, :, (0, 1, 2)] = img[:, :, (2, 1, 0)]
    ax.imshow(img.astype(np.uint8))
    return ax


def plot_bbox_CR(img, bboxes, scores=None, labels=None, thresh=0.5,
                 class_names=None, colors=None, ax=None,
                 reverse_rgb=False, absolute_coordinates=True, approach=None):
    """Visualize bounding boxes.

    Parameters
    ----------
    img : numpy.ndarray or mxnet.nd.NDArray
        Image with shape `H, W, 3`.
    bboxes : numpy.ndarray or mxnet.nd.NDArray
        Bounding boxes with shape `N, 4`. Where `N` is the number of boxes.
    scores : numpy.ndarray or mxnet.nd.NDArray, optional
        Confidence scores of the provided `bboxes` with shape `N`.
    labels : numpy.ndarray or mxnet.nd.NDArray, optional
        Class labels of the provided `bboxes` with shape `N`.
    thresh : float, optional, default 0.5
        Display threshold if `scores` is provided. Scores with less than `thresh`
        will be ignored in display, this is visually more elegant if you have
        a large number of bounding boxes with very small scores.
    class_names : list of str, optional
        Description of parameter `class_names`.
    colors : dict, optional
        You can provide desired colors as {0: (255, 0, 0), 1:(0, 255, 0), ...}, otherwise
        random colors will be substituted.
    ax : matplotlib axes, optional
        You can reuse previous axes if provided.
    reverse_rgb : bool, optional
        Reverse RGB<->BGR orders if `True`.
    absolute_coordinates : bool
        If `True`, absolute coordinates will be considered, otherwise coordinates
        are interpreted as in range(0, 1).

    Returns
    -------
    matplotlib axes
        The ploted axes.

    """
    from matplotlib import pyplot as plt

    if labels is not None and not len(bboxes) == len(labels):
        raise ValueError('The length of labels and bboxes mismatch, {} vs {}'
                         .format(len(labels), len(bboxes)))
    if scores is not None and not len(bboxes) == len(scores):
        raise ValueError('The length of scores and bboxes mismatch, {} vs {}'
                         .format(len(scores), len(bboxes)))

    ax = plot_image(img, ax=ax, reverse_rgb=reverse_rgb)
    #     print(len(bboxes))
    if approach != None:
        plt.title(approach)
    #         ax.set_title(approach, fontdict={'fontsize': 10, 'fontweight': 'medium'})
    if len(bboxes) < 1:
        return ax

    if isinstance(bboxes, mx.nd.NDArray):
        bboxes = bboxes.asnumpy()
    if isinstance(labels, mx.nd.NDArray):
        labels = labels.asnumpy()
    if isinstance(scores, mx.nd.NDArray):
        scores = scores.asnumpy()

    if not absolute_coordinates:
        # convert to absolute coordinates using image shape
        height = img.shape[0]
        width = img.shape[1]
        bboxes[:, (0, 2)] *= width
        bboxes[:, (1, 3)] *= height

    # use random colors if None is provided
    if colors is None:
        colors = dict()
    score_list = []
    xmin1 = []
    ymin1 = []
    xmax1 = []
    ymax1 = []
    co_dict = {'coordinates': {'xmin': xmin1, 'ymin': ymin1, 'xmax': xmax1, 'ymax': ymax1}, 'scores': score_list}
    class_name = ''
    class_list = []
    score = 0
    class_id = None

    for i, bbox in enumerate(bboxes):
        #         print(scores[i], labels[i], bbox)
        if scores is not None and scores[i] < thresh:
            continue
        if labels is not None and labels[i] == "":
            continue
        cls_id = labels[i] if labels is not None else ""
        if cls_id not in colors:
            if class_names is not None:
                colors[cls_id] = plt.get_cmap('hsv')(cls_id / len(class_names))
            else:
                colors[cls_id] = (random.random(), random.random(), random.random())
        xmin, ymin, xmax, ymax = [int(x) for x in bbox]
        rect = plt.Rectangle((xmin, ymin), xmax - xmin,
                             ymax - ymin, fill=False,
                             edgecolor=colors[cls_id],
                             linewidth=3.5)

        ax.add_patch(rect)
        if class_names is not None and cls_id < len(class_names):
            class_list.append(class_names[cls_id])
            class_name = class_names[cls_id]
        else:
            class_name = str(cls_id)
        score = '{:.3f}'.format(scores[i]) if scores is not None else ''
        if class_name or score:
            ax.text(xmin, ymin - 2,
                    '{:s} {:s}'.format(class_name, score),
                    bbox=dict(facecolor=colors[cls_id], alpha=0.5),
                    fontsize=12, color='white')
        score_list.append(score)
        xmin1.append(xmin)
        xmax1.append(xmax)
        ymin1.append(ymin)
        ymax1.append(ymax)
        co_dict = {'coordinates': {'xmin': xmin1, 'ymin': ymin1, 'xmax': xmax1, 'ymax': ymax1}, 'scores': score_list}
        class_id = colors[cls_id]
    #         print("current class list:", class_list)
    return ax, co_dict, class_list, score, class_id, bboxes


import pandas as pd
import ast


def create_inspect_csv(df, output_path):
    column_names = ['image_id', 'prediction', 'ground_truth', 'false_positives']
    column_names2 = ['image_id', 'prediction', 'ground_truth', 'pt_bboxes', 'gt_bboxes']
    result_df = pd.DataFrame(columns=column_names)
    visualization_df = pd.DataFrame(columns=column_names2)
    for index, row in df.iterrows():
        image_id = row['image_id']

        prediction = list(set(row['class_name']))
        gt = list(set(row['gt_class_name']))
        fp = [x for x in prediction if x not in gt]
        # if fp == []:
        #   continue
        data = [[image_id, prediction, gt, fp]]
        print(data)
        data_row = pd.DataFrame(data=data, columns=column_names)
        result_df = result_df.append(data_row, ignore_index=True)

        #         dimension = row['dimension']
        prediction = row['class_name']
        gt = row['gt_class_name']
        p_bbox = row['bboxes']
        gt_bbox = row['gt_bboxes']
        data2 = [[image_id, prediction, gt, p_bbox, gt_bbox]]

        data_row2 = pd.DataFrame(data=data2, columns=column_names2)
        visualization_df = visualization_df.append(data_row2, ignore_index=True)
        # print(new_df['class_name'][0])
    #     result_df.to_csv('Test-Artifacts/' +  backbone + '/regular_fasterRCNN-0.75/predict_truth_report.csv')
    visualization_df.to_csv(output_path, index=False)
    return visualization_df


from sklearn.metrics import confusion_matrix

CLASSES = list({
                   1: u'person', 2: u'bicycle', 3: u'car', 4: u'motorcycle', 5: u'airplane', 6: u'bus', 7: u'train',
                   8: u'truck', 9: u'boat', 10: u'traffic light',
                   11: u'fire hydrant', 12: u'stop sign', 13: u'parking meter', 14: u'bench', 15: u'bird', 16: u'cat',
                   17: u'dog', 18: u'horse', 19: u'sheep', 20: u'cow',
                   21: u'elephant', 22: u'bear', 23: u'zebra', 24: u'giraffe', 25: u'backpack', 26: u'umbrella',
                   27: u'handbag', 28: u'tie', 29: u'suitcase', 30: u'frisbee',
                   31: u'skis', 32: u'snowboard', 33: u'sports ball', 34: u'kite', 35: u'baseball bat',
                   36: u'baseball glove', 37: u'skateboard', 38: u'surfboard', 39: u'tennis racket', 40: u'bottle',
                   41: u'wine glass', 42: u'cup', 43: u'fork', 44: u'knife', 45: u'spoon', 46: u'bowl', 47: u'banana',
                   48: u'apple', 49: u'sandwich', 50: u'orange',
                   51: u'broccoli', 52: u'carrot', 53: u'hot dog', 54: u'pizza', 55: u'donut', 56: u'cake',
                   57: u'chair', 58: u'couch', 59: u'potted plant', 60: u'bed',
                   61: u'dining table', 62: u'toilet', 63: u'tv', 64: u'laptop', 65: u'mouse', 66: u'remote',
                   67: u'keyboard', 68: u'cell phone', 69: u'microwave',
                   70: u'oven', 71: u'toaster', 72: u'sink', 73: u'refrigerator', 74: u'book', 75: u'clock',
                   76: u'vase', 77: u'scissors', 78: u'teddy bear', 79: u'hair drier', 80: u'toothbrush'}
               .values())


def create_confusion_matrix(df, approach):
    inspect_table = create_inspect_csv(df, 'JSON scripts/' + 'truth_table-' + approach + '.csv')
    confusion_columns = ['ground_truth', 'prediction']
    confusion_df = pd.DataFrame(columns=confusion_columns)
    IOU = 0.5
    confusion_dict = {}
    true_match = {}
    fn_dict = {}
    size = len(inspect_table)
    for index, row in inspect_table.iterrows():  # for every image
        print(index, '/', size)
        print(row['image_id'])
        prediction_data = row['pt_bboxes']
        pd_classes = row['prediction']
        ground_truth_data = row['gt_bboxes']
        gt_classes = row['ground_truth']
        gt_match = {}

        for i, bb in enumerate(prediction_data):  # for every pd bbox
            pd_class_name = pd_classes[i]
            print(pd_class_name, bb)
            ovmax = -1
            current_match_idx = -1
            for idx, bbgt in enumerate(ground_truth_data):  # for every gt bbox
                gt_class_name = gt_classes[idx]
                # look for a class_name match
                print('\t--->', gt_class_name, bbgt)
                ov = -1
                # CALCULATE OVERLAP
                bi = [max(bb[0], bbgt[0]), max(bb[1], bbgt[1]), min(bb[2], bbgt[2]),
                      min(bb[3], bbgt[3])]  # intersection bbox
                iw = bi[2] - bi[0] + 1
                ih = bi[3] - bi[1] + 1
                if iw > 0 and ih > 0:
                    # compute overlap (IoU) = area of intersection / area of union
                    ua = (bb[2] - bb[0] + 1) * (bb[3] - bb[1] + 1) + (bbgt[2] - bbgt[0]
                                                                      + 1) * (bbgt[3] - bbgt[1] + 1) - iw * ih
                    ov = iw * ih / ua
                    if ov > ovmax:
                        ovmax = ov
                        current_match_idx = idx  # gt index

                    print('\toverlap:', ov)
                    print('\tmax overlap:', ovmax, 'index:', current_match_idx)
                    print()
            if (ovmax >= IOU):
                if pd_class_name == gt_classes[current_match_idx]:  # same box same class
                    if current_match_idx in gt_match:  # duplicate
                        print("DUPLICATED PREDICTION! ALREADY MATCHED! NOT CONSIDERED!")
                    else:  # new match
                        gt_match[current_match_idx] = i
                        print("A NEW MATCH -> GT: {} and PD: {}".format(current_match_idx, i))
                        if gt_classes[current_match_idx] in true_match:
                            true_match[gt_classes[current_match_idx]].append(pd_class_name)
                        else:
                            true_match[gt_classes[current_match_idx]] = [pd_class_name]
                else:  # same box but different classes
                    print("CONFUSION BETWEEN {} and {}".format(pd_class_name, gt_classes[current_match_idx]))
                    if gt_classes[current_match_idx] in confusion_dict:
                        confusion_dict[gt_classes[current_match_idx]].append(pd_class_name)
                    else:
                        confusion_dict[gt_classes[current_match_idx]] = [pd_class_name]
            else:  # totally different box => extra detection
                print("TOTALLY DIFFERENT BOX")
                print("EXTRA {} DETECTED".format(pd_class_name))
                if 'other' in confusion_dict:
                    confusion_dict['other'].append(pd_class_name)
                else:
                    confusion_dict['other'] = [pd_class_name]
                print()
        print(gt_match.keys())
        matched_gt = gt_match.keys()
        false_negatives = [gt_classes[x] for x in range(len(gt_classes)) if x not in matched_gt]
        print('FALSE NEGATIVES:', false_negatives)
        print('CONFUSION DICT:', confusion_dict)
        print()
        print('########')
        for fn in false_negatives:
            if fn in fn_dict:
                fn_dict[fn] += 1
            else:
                fn_dict[fn] = 1
        # if (index == 100):
        #   break

    y_pred = []
    y_true = []
    print("#######CONFUSION DICT EXPANSION########")
    for gt, preds in confusion_dict.items():
        for pred in preds:
            print("GT: {} <- PD: {}".format(gt, pred))
            y_pred.append(pred)
            y_true.append(gt)
    print("#######REAL MATCH EXPANSION########")
    for gt, preds in true_match.items():
        for pred in preds:
            print("GT: {} <- PD: {}".format(gt, pred))
            y_pred.append(pred)
            y_true.append(gt)
    print("#######FALSE NEGATIVES########")
    print(fn_dict)
    create_fn(fn_dict, approach)
    matrix = confusion_matrix(y_true, y_pred, labels=CLASSES + ['other'])
    df = visualize_matrix(matrix, approach)
    print(df)
    return df


def create_fn(fn_dict, approach):
    fn_df = pd.DataFrame(columns=['false_negatives'])
    for key, value in sorted(fn_dict.items()):
        row_data = pd.DataFrame(data=[[value]], columns=['false_negatives'])
        fn_df = fn_df.append(row_data, ignore_index=True)
    fn_df = fn_df.set_index([pd.Index(sorted(fn_dict.keys()))])
    fn_df.to_csv('JSON scripts/' + '/fn_list-' + approach + '.csv', index=False)
    return fn_df


def visualize_matrix(matrix, approach):
    import seaborn as sn
    import pandas as pd
    import matplotlib.pyplot as plt
    confusion_list = matrix.tolist()
    img_output_path = 'JSON scripts/' + '/confusion_matrix-' + approach + '.png'
    csv_output_path = 'JSON scripts/' + '/confusion_matrix-' + approach + '.csv'
    gt_classes = []
    pt_classes = []
    val_list = []
    new_classes = CLASSES + ['other']
    for i, row in enumerate(confusion_list):
        gt_class = new_classes[i]
        for idx, col in enumerate(row):
            pt_class = new_classes[idx]
            # print(gt_class, pt_class, col)
            gt_classes.append(gt_class)
            pt_classes.append(pt_class)
            val_list.append(col)
    # break
    gt_classes, pt_classes, val_list
    df = pd.DataFrame({'Ground_Truth': gt_classes, 'Prediction': pt_classes, 'Occurences': val_list})
    # df.to_csv('Test-Artifacts/' +  backbone + '/regular_fasterRCNN-0.75/fp_score.csv', index=False)
    df = df.pivot_table(index='Ground_Truth', columns='Prediction', values='Occurences')
    ##MOVE COL###
    cols = list(df)
    print(cols)
    cols.insert(len(cols), cols.pop(47))
    print(cols)
    df = df.reindex(columns=cols)

    ##MOVE ROW###
    rows = df.index.tolist()
    print(rows)
    rows.insert(len(rows), rows.pop(47))
    df = df.reindex(rows)
    df.to_csv(csv_output_path, index=True)
    print(df)
    plt.figure(figsize=(30, 15))
    sn.heatmap(df, annot=True, annot_kws={"size": 17}, cmap='CMRmap', cbar=False)
    plt.savefig(img_output_path)
    return df


for idx, df in enumerate(df_list):
    approach = label_list[idx]
    create_confusion_matrix(df, approach)
