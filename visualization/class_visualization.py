import os
import pandas as pd

class_level_list = os.listdir('outputs/')
data_list = [each.replace('_output.txt', '') for each in class_level_list]

for file in class_level_list:
    data_frame = pd.read_csv('outputs/' + file)
    for _, row in data_frame.iterrows():
        with open('classes/' + row.class_name + '.txt', 'a+') as f:
            f.write(file.replace('_output.txt', '').lower() + ',' + str(row.mAP)+'\n')
            f.close()
