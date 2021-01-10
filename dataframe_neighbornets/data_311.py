import json
import pandas as pd

file_path = r"C:\Users\chara\Documents\Data\311_Data\1672BG_Shape.json"
df_path = r"C:\Users\chara\Documents\Data\All_Data_Nbh_ID\311_Call_Center_Service_Requests.csv"
new_df_path = r"C:\Users\chara\Documents\Data\All_Data_Nbh_ID\processed.csv"

data_311 = pd.read_csv(df_path)
with open(file_path, 'r') as f:
    geo_json = json.load(f)


def map_neighborhood(input):
    print(f'processing {input["CASE ID"]}')
    lattitude, longtitude = input['LATITUDE'], input['LONGITUDE']
    for each in geo_json.keys():
        right_top, right_bottom = False, False
        left_top, left_bottom = False, False
        list_geo_points = geo_json[each]['BOUNDARIES']
        for each_point in list_geo_points:
            if lattitude < each_point[0] and longtitude < each_point[1]:
                right_top = True
            if lattitude < each_point[0] and longtitude > each_point[1]:
                right_bottom = True
            if lattitude > each_point[0] and longtitude > each_point[1]:
                left_bottom = True
            if lattitude > each_point[0] and longtitude < each_point[1]:
                left_top = True
            if right_top and right_bottom and left_top and left_bottom:
                print(f'block id : {each} - processing {input["CASE ID"]}')
                return each


data_311["block_id"] = data_311.apply(map_neighborhood, axis=1)
data_311.to_csv(new_df_path, header=True, index=False)
print("values finished")
