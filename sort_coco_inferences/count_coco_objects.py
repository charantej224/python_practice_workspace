import json
import os

gt_path = "/home/charan/Documents/research/deep_lite/current_work/annotations_trainval2017/annotations/instances_val2017.json"
# output_path = "/home/charan/Documents/task_to_do/JSON scripts"
output_path = "/home/charan/Documents/verify"
# backbones = ["resnet50", "resnet101"]


backbones = ["resnet50"]


def count_ground_truth():
    with open(gt_path, 'r') as f:
        instances = json.load(f)
        f.close()

    print(len(instances["annotations"]))


def return_output_dict(inner_path):
    with open(inner_path, 'r') as f:
        output_dict = json.load(f)
        f.close()
        return output_dict


def category_id_level(approach, inference_list):
    parent_dict = {}
    if approach not in parent_dict:
        parent_dict[approach] = {}
    for each in inference_list:
        cat_dict = parent_dict[approach]
        if each["category_id"] not in cat_dict:
            cat_dict[each["category_id"]] = 0
        cat_dict[each["category_id"]] += 1
        parent_dict[approach] = cat_dict

    for key, value in parent_dict.items():
        print(key, "\n")
        for in_key in sorted(value.keys()):
            print(f'{str(in_key)} - {str(value[in_key])}')


def count_outputs():
    for each in backbones:
        path = os.path.join(output_path, each)
        for each_dir in os.listdir(path):
            if "output" in each_dir:
                inner = os.path.join(path, each_dir)
                dict = return_output_dict(inner)
                category_id_level(each_dir, dict)
                print(f'{each} - {each_dir} - {len(dict)}')


if __name__ == "__main__":
    count_outputs()
