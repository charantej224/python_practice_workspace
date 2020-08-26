import pandas as pd
from xlwt import Workbook
import os

current_run_folder = "resnet101/"

resnet_files_list = os.listdir(current_run_folder)

df_dict = {}

for each in resnet_files_list:
    data_frame = pd.read_csv(current_run_folder + each)
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
    max_val, min_val = output_dataframe["value"].max(), output_dataframe["value"].min()
    output_dataframe["normalized"] = (output_dataframe["value"] - min_val) / (max_val - min_val)
    output_dataframe["normalized"] = output_dataframe["normalized"].round(decimals=2)
    output_dataframe.to_csv("confused_pairs.csv",index=False)
    output_dataframe1 = pd.DataFrame.from_dict(class_confusion_rate, orient='index', columns=["confusions_involved"])
    output_dataframe1 = output_dataframe1.sort_values(by=['confusions_involved'], ascending=False)
    # output_dataframe1 = output_dataframe1.reset_index(drop=True)

    df_dict[each] = output_dataframe
    df_dict[each + "_confusion_rates"] = output_dataframe1
    print(f'finished {each}')

with pd.ExcelWriter(current_run_folder.replace("/", "") + '.xlsx', engine="openpyxl", mode='w') as writer:
    for key, value in df_dict.items():
        value.to_excel(writer, sheet_name=key)
