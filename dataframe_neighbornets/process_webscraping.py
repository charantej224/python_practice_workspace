import os
import pandas as pd

root_dir = "/home/charan/Documents/workspaces/python_workspaces/Data/ADL_Project/scraped_data"
total_data = os.path.join(root_dir, 'final.csv')

list_files = os.listdir(root_dir)
list_pandas = []

for each in list_files:
    abs_path = os.path.join(root_dir, each)
    list_pandas.append(pd.read_csv(abs_path))

merge_data = pd.concat(list_pandas)
merge_data.drop(columns=['CASE_ID'], inplace=True)
merge_data.drop_duplicates(inplace=True)
merge_data.to_csv(total_data, header=True, index=False)

print(len(list(merge_data["CASE ID"].unique())))
