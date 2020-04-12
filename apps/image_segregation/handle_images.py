import shutil
from os import listdir

input_path = "/home/charan/Downloads/Charan_Test/Images/"
output_path = "/home/charan/Downloads/Charan_Test/segregated_images/"

image_per_segregation = 50
count = 1
internal_count = 0

import os

for file in listdir(input_path):
    if internal_count >= image_per_segregation:
        count += 1
        internal_count = 0
    dest_path = output_path + str(count) + "/"
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    shutil.move(input_path + file, dest_path)
    print('input - {}, output {}'.format(input_path + file, dest_path))
    internal_count += 1

