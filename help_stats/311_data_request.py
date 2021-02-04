import pandas as pd
import os

desc_path = "/home/charan/DATA/311_Data/311_VIZ_DESCRIPTION_PARENT.csv"
full_desc_path = "/home/charan/DATA/311_Data/311_call_2007_2020_Neighborhood.csv"
path = "/home/charan/DATA/311_Data/Analysis"
trash_dept = ['City Managers Office', 'NHS', 'Public Works', 'Parks and Rec', 'Water Services', 'Northland']
new_desc_path = os.path.join(path, "Desc_Data")
desc_path_group = os.path.join(new_desc_path, "group_dept.csv")
whole_path = os.path.join(path, 'whole')
whole_path_group = os.path.join(whole_path, "grouped_whole.csv")


def trash_analysis():
    data_visible = pd.read_csv(desc_path)
    id_neigh = data_visible[data_visible.nbh_id.notna()]
    non_id_neigh = data_visible[data_visible.nbh_id.isna()]
    print(id_neigh.shape)
    print(non_id_neigh.shape)
    new_df = data_visible[data_visible.CATEGORY.apply(lambda x: 'Trash' in x)]
    for each in trash_dept:
        temp_df = new_df[new_df.DEPARTMENT == each].reset_index()
        each = each.replace(" ", "_") + ".csv"
        each = os.path.join(path, each)
        temp_df.to_csv(each, index=False)
    print("finished")


def desc_data():
    data_visible = pd.read_csv(desc_path)
    id_neigh = data_visible[data_visible.nbh_id.notna()]
    non_id_neigh = data_visible[data_visible.nbh_id.isna()]
    # group_by_df = data_visible.groupby(by=['DEPARTMENT'])['CASE ID'].count().reset_index(name="count")
    group_by_df = data_visible.groupby(by=['CREATION YEAR'])['CASE ID'].count().reset_index(name="count")
    group_by_df.to_csv(desc_path_group, index=False)
    print(id_neigh.shape)


def full_data():
    full_desc_data = pd.read_csv(full_desc_path)
    id_neigh = full_desc_data[full_desc_data.nbh_id.notna()]
    non_id_neigh = full_desc_data[full_desc_data.nbh_id.isna()]
    print(id_neigh.shape)
    print(non_id_neigh.shape)
    # group_by_df = full_desc_data.groupby(by=['DEPARTMENT'])['CASE ID'].count().reset_index(name="count")
    group_by_df = full_desc_data.groupby(by=['CREATION YEAR'])['CASE ID'].count().reset_index(name="count")
    group_by_df.to_csv(whole_path_group, index=False)
    print(id_neigh.shape)
    whole_path_group


if __name__ == '__main__':
    full_data()
