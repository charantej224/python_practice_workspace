import json

source_annotation_file = '/home/charan/Documents/research/annotations_trainval2017/annotations/instances_val2017.json'

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
images_list = []
licenses_list = []
annotations_list = []
file_list = []
license_id_list = []
image_id_list = []

with open('image_ids.txt', 'r') as f:
    image_id_list = f.readlines()

for i in range(len(image_id_list)):
    image_id_list[i] = image_id_list[i].strip('\n')

for image_dict in content_dict_1000_images['images']:
    if image_dict['file_name'] in image_id_list:
        images_list.append(image_dict)

content_dict_1000_images['images'] = images_list

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

with open('file_output_1000_images_new.json', 'w') as selected_images_json:
    selected_images_json.write(pp_json(content_dict_1000_images))

with open('image_ids_new.txt', 'w') as f:
    f.write('\n'.join(file_list))

num_categories = len(content_dict_1000_images['categories'])
num_licenses = len(content_dict_1000_images['licenses'])
num_annotations = len(content_dict_1000_images['annotations'])
num_images = len(content_dict_1000_images['images'])

print(f'num_categories list {num_categories}')
print(f'num_licenses list {num_licenses}')
print(f'num_annotations list {num_annotations}')
print(f'num_images list {num_images}')

