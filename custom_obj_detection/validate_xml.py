import xml.etree.ElementTree as ET

# xml_file = '/home/charan/Documents/workspaces/aeroplane/aeroplane/Datasets/VOC2007/Annotations/000032.xml'
# annotations = ET.parse(xml_file)
# root = annotations.getroot()

# for each in root.iter('object'):
#    print(each.find('bndbox/xmin').text)

import os

root_dir = '/home/charan/Documents/workspaces/aeroplane/aeroplane/Datasets/VOC2007/'
image_sets = open(os.path.join(root_dir, 'ImageSets/Main/validation.txt'), 'r')

for each in image_sets.readlines():
    print(each.strip())
