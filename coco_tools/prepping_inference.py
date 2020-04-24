import json
import pandas as pd
import ast

category_df = pd.read_csv('category_ids.csv')
# print(category_df)
category_df = category_df.drop(columns=['object_x', 'object_y', 'object_z'])
cat_dict = category_df.set_index('object').to_dict()
cat_dict = cat_dict['id']
# print(cat_dict)

inference_df = pd.read_csv('inference_metrics_lite.csv')

output_key1 = "image_id"
output_key2 = "category_id"
output_key3 = "bbox"
output_key4 = "score"

input_key1 = "image_id"
input_key2 = "class_name"
input_key3 = "bboxes"
input_key4 = "scores"

final_list = []
list_missing_cat_ids = []


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
    if len(category_ids) == 0:
        list_missing_cat_ids.append(image_id)
        print(f'no category ids, so not writing this into json for : {each_row}')
        return
    for counter in range(len(category_ids)):
        row_dict = {output_key1: int(image_id.replace('.jpg', '')), output_key2: int(cat_dict[category_ids[counter]])}
        boxes = bbox[counter]
        row_dict[output_key3] = [boxes[0], boxes[1], boxes[2] - boxes[0], boxes[3] - boxes[1]]
        row_dict[output_key4] = float(score[counter])
        final_list.append(row_dict)


for _, each_row in inference_df.iterrows():
    # print(each_row)
    handle_each_row(each_row)

with open('output.json', 'w') as f:
    f.write(pp_json(final_list))

print(list_missing_cat_ids)
