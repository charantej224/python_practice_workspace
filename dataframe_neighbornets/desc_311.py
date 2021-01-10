import pandas as pd
import json

whole_df = r"C:\Users\chara\Documents\Data\311_Data\311_NEIGH_VIS_NONVIS_v1.csv"
desc_df = r"C:\Users\chara\Documents\Data\311_Data\SAMPLE_311_DATA_CRM_PROB_DESC_ONLY.csv"
merged = r"C:\Users\chara\Documents\Data\311_Data\311_merged.csv"
df_path = r"C:\Users\chara\Documents\Data\All_Data_Nbh_ID\311_Call_Center_Service_Requests.csv"


def read_data():
    data = pd.read_csv(df_path)
    print(data.shape)


def merge_data():
    desc_data = pd.read_csv(desc_df, encoding="latin-1")
    desc_data = desc_data.loc[:, ~desc_data.columns.str.contains('^Unnamed')]
    whole_data = pd.read_csv(whole_df)
    desc_data.drop(columns=['Status'], inplace=True)
    desc_data.rename(columns={"Case": "CASE ID"}, inplace=True)
    new_df = whole_data.merge(desc_data, on=["CASE ID"])
    new_df = new_df[new_df['Description'].notna()]
    new_df.to_csv(merged, index=False)


def stats_data():
    whole_data = pd.read_csv(whole_df)
    print("shape whole data {}".format(whole_data.shape))
    merged_data = pd.read_csv(merged)
    print("shape merged data {}".format(merged_data.shape))


def read_json():
    with open(r'C:\Users\chara\Documents\Data\311_Data\1672BG_Shape.json', 'r') as f:
        geo_dict = json.load(f)
        f.close()
    counter = 0
    for each in geo_dict.keys():
        if each.startswith('29'):
            counter += 1
    print(geo_dict)


if __name__ == '__main__':
    read_data()
