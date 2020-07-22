import json
import pandas as pd
import ast
from pycocotools.coco import COCO

category_df = pd.read_csv('category_ids.csv')
# print(category_df)
category_df = category_df.drop(columns=['object_x', 'object_y', 'object_z'])
cat_dict = category_df.set_index('object').to_dict()
cat_dict = cat_dict['id']
# print(cat_dict)

inference_df = pd.read_csv('inference_metrics_anova.csv')

output_key1 = "image_id"
output_key2 = "category_id"
output_key3 = "bbox"
output_key4 = "score"

input_key1 = "image_id"
input_key2 = "class_name"
input_key3 = "bboxes"
input_key4 = "scores"
input_key5 = "dimension"

final_list = []
list_missing_cat_ids = []

annType = ['segm', 'bbox', 'keypoints']
annType = annType[1]  # specify type here
prefix = 'person_keypoints' if annType == 'keypoints' else 'instances'

dataType = 'val2017'
annFile = '/home/charan/Documents/research/deep_lite/current_work/annotations_trainval2017/annotations/%s_%s.json' % (
    prefix, dataType)
cocoGt = COCO(annFile)


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        return json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents)
    else:
        return json.dumps(json_thing, sort_keys=sort, indent=indents)
    return None


def handle_each_row(each_row):
    image_id = each_row[input_key1]
    category_ids = ast.literal_eval(each_row[input_key2])
    bbox = ast.literal_eval(each_row[input_key3])
    score = ast.literal_eval(each_row[input_key4])
    dimensions = ast.literal_eval(each_row[input_key5])
    inference_width, inference_height = dimensions[0], dimensions[1]
    if len(category_ids) == 0:
        list_missing_cat_ids.append(image_id)
        print(f'no category ids, so not writing this into json for : {each_row}')
        return
    for counter in range(len(category_ids)):
        row_dict = {output_key1: int(image_id.replace('.jpg', '')), output_key2: int(cat_dict[category_ids[counter]])}
        boxes = bbox[counter]
        image = cocoGt.loadImgs([int(image_id.replace('.jpg', ''))])
        original_width, original_height = image[0]['width'], image[0]['height']
        # Original predicted values.
        x_min, y_min, x_max, y_max = float(boxes[0]), float(boxes[1]), float(boxes[2]), float(boxes[3])
        x_min = 0 if x_min < 0 else x_min
        y_min = 0 if y_min < 0 else y_min
        x_max = 0 if x_max < 0 else x_max
        y_max = 0 if y_max < 0 else y_max

        # scaling factor variables.
        x_factor, y_factor = original_width / inference_width, original_height / inference_height
        # (xmin/ inference-width )*original_width = newx_min
        # re-scaled parameters.
        x_min_s, y_min_s, x_max_s, y_max_s = x_min * x_factor, y_min * y_factor, x_max * x_factor, y_max * y_factor

        row_dict[output_key3] = [x_min_s, y_min_s, x_max_s - x_min_s, y_max_s - y_min_s]
        row_dict[output_key4] = float(score[counter])
        final_list.append(row_dict)


for _, each_row in inference_df.iterrows():
    # print(each_row)
    handle_each_row(each_row)

with open('output.json', 'w') as f:
    f.write(pp_json(final_list))

print(list_missing_cat_ids)
