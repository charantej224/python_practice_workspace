import pandas as pd
import os

from utils.file_utils import write_dict

root_dir = "/home/charan/DATA/311_Data/multi-level-classification"
interested_df = os.path.join(root_dir, "multi-level.csv")
df_data = os.path.join(root_dir, "311_VIZ_DESCRIPTION_PARENT.csv")
grouped = os.path.join(root_dir, "group.csv")
balanced = os.path.join(root_dir, "balanced_multi-level.csv")
json_category = os.path.join(root_dir, "category_class.json")
json_type = os.path.join(root_dir, "type_class.json")


def analyze_data():
    data = pd.read_csv(df_data)
    grouped_data = data.groupby(by=["PARENT_CATEGORY", "TYPE"])["CASE ID"].count().reset_index(name="COUNT")
    grouped_data.to_csv(grouped, index=False)
    new_df = data[['CASE ID', 'PARENT_CATEGORY', 'TYPE', 'Description']]
    new_df.to_csv(interested_df, index=False)


def add_data(input_df, number):
    while input_df.shape[0] < number:
        input_df = pd.concat([input_df, input_df])
    if input_df.shape[0] > number:
        input_df = input_df[:number]
    return input_df


def balance_data():
    data = pd.read_csv(interested_df)
    list_types = list(data.TYPE.unique())
    list_df_types = []
    for df_type in list_types:
        each_df = data[data.TYPE == df_type]
        if each_df.shape[0] > 200:
            each_df = each_df[:200]
        if each_df.shape[0] < 200:
            each_df = add_data(input_df=each_df, number=200)
        list_df_types.append(each_df)
    balanced_df = pd.concat(list_df_types)
    balanced_df.to_csv(balanced, index=False)
    print("finished")


def check_balanced():
    data = pd.read_csv(balanced)
    group = data.groupby(by='TYPE')['CASE ID'].count().reset_index()
    print("finished")


def get_classes():
    cat_dict, type_dict = {}, {}
    data = pd.read_csv(balanced)
    type_list = sorted(list(data['TYPE'].unique()))
    cat_list = sorted(list(data['PARENT_CATEGORY'].unique()))
    counter = 0
    for each_type in type_list:
        type_dict[each_type] = counter
        type_dict[str(counter)] = each_type
        counter += 1
    counter = 0
    for each_category in cat_list:
        cat_dict[each_category] = counter
        cat_dict[str(counter)] = each_category
        counter += 1
    write_dict(cat_dict, json_category)
    write_dict(type_dict, json_type)


if __name__ == '__main__':
    get_classes()
