import json

source_annotation_file = '/home/charan/Documents/research/annotations_trainval2017/annotations/person_keypoints_val2017.json'

content_dict_1000_images = {}


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        return json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents)
    else:
        return json.dumps(json_thing, sort_keys=sort, indent=indents)
    return None


# keys
# info, licenses, images , annotations, categories

with open(source_annotation_file, 'r') as source:
    json_content = json.load(source)

content_dict_1000_images['info'] = json_content['info']
content_dict_1000_images['categories'] = json_content['categories']
content_dict_1000_images['images'] = json_content['images'][:1000]

licenses_list = []
annotations_list = []
file_list = []
license_id_list = []
image_id_list = []

for each_image_dict in content_dict_1000_images['images']:
    file_list.append(each_image_dict['file_name'])
    license_id_list.append(each_image_dict['license'])
    image_id_list.append(each_image_dict['id'])

for each_license_dict in json_content['licenses']:
    if each_license_dict['id'] in license_id_list:
        licenses_list.append(each_license_dict)

for each_annotation_list in json_content['annotations']:
    if each_annotation_list['image_id'] in image_id_list:
        annotations_list.append(each_annotation_list)

content_dict_1000_images["licenses"] = licenses_list
content_dict_1000_images["annotations"] = annotations_list

with open('file_output_1000_images.json', 'w') as selected_images_json:
    selected_images_json.write(pp_json(content_dict_1000_images))

with open('image_ids.txt', 'w') as f:
    f.write('\n'.join(file_list))
