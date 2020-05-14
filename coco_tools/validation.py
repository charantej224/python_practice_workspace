id = 252219

file = "file_output_1000_images_new.json"

import json

with open(file, 'r') as f:
    valid_dict = json.load(f)

i = 0

for each_dict in valid_dict['annotations']:
    if each_dict['image_id'] == id:
        i += 1

print(i)
