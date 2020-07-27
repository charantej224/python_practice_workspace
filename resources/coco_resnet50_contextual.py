import ast
import glob
import time
import pandas as pd
import gluoncv as gcv
import matplotlib.pyplot as plt
from pathlib import Path
from tqdm import tqdm
import mxnet as mx
import os
from resources.bbox_context import plot_bbox
import os.path as path

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

with open('context_list.txt', 'r') as f:
    ctx_list = ast.literal_eval(f.readlines()[0])
print(ctx_list)
# artifact_path = 'Test-Artifacts/' + backbone + '/Contextual/0.95/' 
# output_path = artifact_path +'output/'
# Path(output_path).mkdir(parents=True, exist_ok=True)


"""# **1. Generate Test Datasets**"""
img_directory = '/home/charan/Documents/research/deep_lite/current_work/val2017/'  # structure coco testset directory
img_path = img_directory + '*.jpg'
imglist = glob.glob(img_path)
print(imglist)

"""# **2. Inferencing and Creating inference metrics**

*2b. Inferencing based on calculated thresholds
"""
backbone = "test-2017"

max_image_per_run = 1

if path.exists("state.txt"):
    with open("state.txt", "w") as f:
        state = f.read()
        if state != "completed":
            print("script exited as instance of script is already running.")
            exit(0)


def write_file(state):
    with open("state.txt", "w") as f:
        f.write(state)
        f.close()


write_file("running")


# edit: add threshold as a parameter in each class, create and save dataframes for each class
def inference(threshold):
    column_names = ['image_id', 'dimension', 'class_name', 'inference_time', 'bboxes', 'scores']

    df = pd.DataFrame(columns=column_names)
    artifact_path = 'Test-Artifacts/' + backbone + '/Contextual/' + str(threshold) + '/'
    output_path = artifact_path + 'output/'
    csv_path = artifact_path + 'inference_metrics_co_occurances.csv'
    Path(output_path).mkdir(parents=True, exist_ok=True)
    print(output_path)
    if os.path.exists(csv_path):
        # print('EXISTS CSV!')
        # os.remove(csv_path)
        # df = pd.DataFrame(columns = column_names)
        # df_size = 0

        df = pd.read_csv(csv_path)
        df_size = len(df)
    else:
        print('NOT EXISTS!')
        df_size = 0
    print(df_size)

    counter = 0
    for index, filename in enumerate(tqdm(imglist)):
        if index < df_size:
            continue

            # if index == 10:
            #   break
        start_time = time.time()
        img_path = filename
        img_score_list = []
        img_bbox_list = []
        img_class_list = []

        for idx, group in enumerate(ctx_list):
            print("CURRENT MODEL: ", group)
            ctx = mx.gpu(0)
            net = gcv.model_zoo.get_model('yolo3_darknet53_voc@416', pretrained=True, ctx=ctx)
            net.reset_class(classes=group, reuse_weights=group)

            x, image = gcv.data.transforms.presets.rcnn.load_test(img_path, 640)
            cids, scores, bboxes = net(x.as_in_context(ctx))

            ax, co_dict, class_name, score, color, bbox = plot_bbox(image, bboxes[0], scores[0], cids[0],
                                                                    class_names=group,
                                                                    thresh=threshold)
            image_id = filename.split('/')[-1]
            coordinate_list = []
            score_list = []
            # Extract Prediction Coordinates
            for j in range(0, len(co_dict['coordinates']['xmin'])):
                xmin = co_dict['coordinates']['xmin'][j]
                ymin = co_dict['coordinates']['ymin'][j]
                xmax = co_dict['coordinates']['xmax'][j]
                ymax = co_dict['coordinates']['ymax'][j]
                score = co_dict['scores'][j]
                coordinate_list.append([xmin, ymin, xmax, ymax])

                score_list.append(score)

            width = plt.xlim()[1] - plt.xlim()[0]
            height = plt.ylim()[0] - plt.ylim()[1]

            # Create a dataframe based on predicted results v
            # data = [[image_id,[width, height], class_list, str(time.time() - start_time), coordinate_list, score_list ]]
            # data_df = pd.DataFrame(data, columns = column_names)

            plt.savefig(output_path + image_id)
            plt.close()
            img_score_list += score_list
            img_class_list += class_name
            img_bbox_list += coordinate_list

        row_data = [
            [image_id, [width, height], img_class_list, str(time.time() - start_time), img_bbox_list, img_score_list]]
        print(row_data)
        data_df = pd.DataFrame(row_data, columns=column_names)
        df = df.append(data_df, ignore_index=True)
        df.to_csv(csv_path, index=False)
        ctx.empty_cache()
        counter += 1
        if counter >= max_image_per_run:
            break

    # break
    print(df)


inference(0.8)
write_file("completed")
