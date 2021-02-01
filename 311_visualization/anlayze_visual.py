import os
import pandas as pd

from utils.file_utils import read_json

root_dir = "/home/charan/DATA/311_Data/visualization/VIZ_Classification"
viz_data = os.path.join(root_dir, "311_VIZ_DESCRIPTION.csv")
class_json = os.path.join(root_dir, "class.json")
predicted = os.path.join(root_dir, "predicted.csv")
class_json = read_json(class_json)
predicted_details = os.path.join(root_dir, "Predicted_Details.csv")


def merge_data():
    parent_df = pd.read_csv(viz_data)
    predicted_df = pd.read_csv(predicted)
    predicted_df["original"] = predicted_df["original"].apply(lambda x: class_json[str(int(x))])
    predicted_df["predicted"] = predicted_df["predicted"].apply(lambda x: class_json[str(int(x))])
    predicted_df.rename(columns={"id": "CASE ID"}, inplace=True)
    parent_sub_set = parent_df[
        ['CASE ID', 'CATEGORY', 'TYPE', 'DEPARTMENT', 'WORK GROUP', 'REQUEST TYPE', 'Description']]
    final_df = predicted_df.merge(parent_sub_set, on=['CASE ID'], how="left")
    final_df.to_csv(predicted_details, index=False)


if __name__ == '__main__':
    merge_data()
