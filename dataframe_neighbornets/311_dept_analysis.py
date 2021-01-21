import pandas as pd
import copy

from utils.file_utils import write_dict, read_json

root_dir = "/home/charan/DATA/311_Data/New_Department/311_VIZ_DESCRIPTION.csv"
root_dir_parent = "/home/charan/DATA/311_Data/New_Department/311_VIZ_DESCRIPTION_PARENT.csv"
root_dir_parent_balanced = "/home/charan/DATA/311_Data/New_Department/311_VIZ_DESCRIPTION_PARENT_BAL.csv"
reference = "/home/charan/DATA/311_Data/New_Department/department.csv"
parent_json = "/home/charan/DATA/311_Data/New_Department/parent_map.json"
class_json = "/home/charan/DATA/311_Data/New_Department/class.json"

parent_map = read_json(parent_json)


def make_it(input_df, number):
    while True:
        input_df = pd.concat([input_df, copy.deepcopy(input_df)])
        if input_df.shape[0] > number:
            return input_df[:number]


def read_data():
    list_data = []
    dept_data = pd.read_csv(root_dir_parent)
    unique_dept = list(dept_data.PARENT_DEPT.unique())
    for each in unique_dept:
        each_df = dept_data[dept_data.PARENT_DEPT == each]
        if each_df.shape[0] < 15000:
            each_df = make_it(each_df, 15000)
        elif each_df.shape[0] > 40000:
            each_df = make_it(each_df, 40000)
        list_data.append(each_df)
        print(f'{each},{each_df.shape[0]}')
    final_df = pd.concat(list_data)
    final_df.to_csv(root_dir_parent_balanced, index=False)
    print("finished")


def record_error_data():
    records_dict = {}
    class_dict = {}
    counter = 0
    ref_df = pd.read_csv(reference).to_dict('records')
    for each in ref_df:
        if each['group'] not in records_dict:
            records_dict[each['group']] = []
        records_dict[each['group']].append(each['original'])

    for each in list(records_dict.keys()):
        class_dict[str(counter)] = each
        class_dict[each] = counter
        counter += 1

    write_dict(records_dict, parent_json)
    write_dict(class_dict, class_json)
    print("finished")


def apply_dept(input_val):
    for each in parent_map.keys():
        list_values = parent_map[each]
        if any(input_val in val for val in list_values):
            return each


def analyze_data_imbalance():
    dept_data = pd.read_csv(root_dir)
    dept_data['PARENT_DEPT'] = dept_data.DEPARTMENT.apply(apply_dept)
    dept_data.to_csv(root_dir_parent, index=False)


if __name__ == '__main__':
    read_data()
