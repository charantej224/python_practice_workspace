import pandas as pd


def assignment_problem():
    path = "/home/charan/DATA/311_Data/Boundary/311_call_data.csv"
    path1 = "/home/charan/DATA/311_Data/Boundary/group_by.csv"
    data_311 = pd.read_csv(path)
    grouped_df = data_311.groupby(by="CATEGORY")['CASE ID'].count().reset_index(name='count')
    grouped_df.to_csv(path1, index=False, header=True)
    print("finished")


def mapping_problem():
    path = "/home/charan/DATA/311_Data/311_Block_Group_Processed.csv"
    path2 = "/home/charan/DATA/311_Data/Boundary/311_call_data.csv"
    data_311 = pd.read_csv(path)
    data_two_311 = pd.read_csv(path2)
    print(data_311.shape, data_two_311.shape)
    print("finished")


def neighborhood_map():
    path = "/home/charan/DATA/311_Data/311_call_2007_2020_Neighborhood.csv"
    data_311 = pd.read_csv(path)
    new_df = data_311.groupby(by=['NEIGHBORHOOD', 'nbh_name'])['CASE ID'].count().reset_index(name='count')
    new_df.to_csv('/home/charan/DATA/311_Data/group_map.csv', header=True, index=False)
    print('finished')


def parent_map():
    path = "/home/charan/DATA/311_Data/311_VIZ_DESCRIPTION_PARENT.csv"
    data_311 = pd.read_csv(path)
    path = "/home/charan/DATA/311_Data/cat_stats.csv"
    cat_stat = data_311.groupby(by=['CATEGORY', 'PARENT_CATEGORY'])['CASE ID'].count().reset_index(name='count')
    cat_stat.to_csv(path, header=True, index=False)
    print("finished")


if __name__ == '__main__':
    parent_map()
