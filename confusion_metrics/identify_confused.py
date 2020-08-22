import pandas as pd
from xlwt import Workbook
import os

resnet50_list = os.listdir("resnet50")
resnet101_list = os.listdir("resnet101")

df_dict = {}

for each in resnet50_list:
    data_frame = pd.read_csv("resnet50/" + each)
    data_frame = data_frame.drop(index=80)
    data_frame = data_frame.drop("other", axis=1)
    classes = data_frame['Ground_Truth'].tolist()
    row_list = []
    class_confusion_rate = {}
    for out_each in classes:
        for in_each in range(len(classes)):
            if out_each != classes[in_each] and data_frame[out_each][in_each] > 0:
                dict_val = {
                    'predicted_class': out_each,
                    'actual_class': classes[in_each],
                    'value': data_frame[out_each][in_each]
                }
                row_list.append(dict_val)
                if out_each not in class_confusion_rate:
                    class_confusion_rate[out_each] = 0
                if classes[in_each] not in class_confusion_rate:
                    class_confusion_rate[classes[in_each]] = 0
                class_confusion_rate[out_each] += data_frame[out_each][in_each]
                class_confusion_rate[classes[in_each]] += data_frame[out_each][in_each]
                print(out_each, classes[in_each], data_frame[out_each][in_each])
    output_dataframe = pd.DataFrame(row_list, columns=['actual_class', 'predicted_class', 'value'])
    output_dataframe = output_dataframe.sort_values(by=['value'], ascending=False)
    output_dataframe = output_dataframe.reset_index(drop=True)
    output_dataframe1 = pd.DataFrame.from_dict(class_confusion_rate, orient='index',columns=["confusions_involved"])
    output_dataframe1 = output_dataframe1.sort_values(by=['confusions_involved'], ascending=False)
    # output_dataframe1 = output_dataframe1.reset_index(drop=True)

    df_dict[each] = output_dataframe
    df_dict[each + "_confusion_rates"] = output_dataframe1
    print(f'finished {each}')

with pd.ExcelWriter('resnet50_confusion.xlsx', engine="openpyxl", mode='w') as writer:
    for key, value in df_dict.items():
        value.to_excel(writer, sheet_name=key)

