'''
Author : Charan Tej
ID     : <Unique ID>
contact : @gmail.com
Copyrights :
Description: reads data from file and converts  into a dataframe for numerial analysis.
'''
import pandas as pd
import ast
import random


def convert_values(file_name):
    '''
    convert_values : this function is intended to read values and convert them into pandas (dataframes).
    :input: file_name (String) - name of the file.
    :return: final_df - Dataframe with processed file data.
    '''
    with open('inference.csv', 'r') as f:
        records = f.readlines()

    final_list = []

    for i in range(len(records)):
        record_dict = {}
        each_row = records[i].strip('\n')
        row_list = each_row.split(',')
        record_dict['image_id'] = row_list[0]
        each_row = each_row.replace(row_list[0], '')
        row_list = each_row.split('],[')
        bboxes = ast.literal_eval('[' + row_list[1])
        for i in range(len(bboxes)):
            bboxes[i] = [bboxes[i][0][0], bboxes[i][0][1], bboxes[i][1][0], bboxes[i][1][1]]
        record_dict['bboxes'] = bboxes
        classes = row_list[0] + ']'
        print(classes[1:])
        record_dict['class_name'] = ast.literal_eval(classes[1:])
        record_dict['scores'] = [check_random() for x in record_dict['class_name']]

        final_list.append(record_dict)

    final_df = pd.DataFrame(final_list, columns=['image_id', 'class_name', 'bboxes', 'scores'])
    final_df.to_csv('inference_metrics_co_occurances.csv', index=False, header=True)


def read_output():
    data_frame = pd.read_csv('inference_metrics.csv')
    print(data_frame)


def check_random():
    return round(random.uniform(0.8, 1), 3)


if __name__ == "__main__":
    convert_values()
