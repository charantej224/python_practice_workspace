import json
import pandas as pd
import threading

file_path = "/home/charan/DATA/311_Data/Boundary_analysis/1672BG_Shape.json"
df_path = "/home/charan/DATA/311_Data/Boundary_analysis/311_call_data.csv"
new_df_path = "/home/charan/DATA/311_Data/Boundary_analysis/{}_processed.csv"

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


def boundary_mapping(input_key, input_data_311):
    print("boundary processing started {}".format(input_key))
    final_df_path = new_df_path.format(input_key)
    input_data_311["block_id"] = input_data_311.apply(map_neighborhood, axis=1)
    input_data_311.to_csv(final_df_path, header=True, index=False)
    print("{} values finished".format(input_key))


def boundary_map():
    data_311 = pd.read_csv(df_path)
    list_years = list(data_311['CREATION YEAR'].unique())
    for each in list_years:
        each_df = data_311[data_311['CREATION YEAR'] == each]
        x = threading.Thread(target=boundary_mapping, args=(each, each_df,))
        x.start()


def stats_data():
    df_path = "/home/charan/DATA/311_Data/311_Block_Group_Processed.csv"
    block_data = pd.read_csv(df_path)
    list_types = list(block_data.TYPE.unique())
    for each in list_types:
        each_df = block_data[block_data["TYPE"] == each]
        not_mapped = each_df[each_df['block_id'].isna()].shape[0]
        mapped = each_df[each_df['block_id'].notna()].shape[0]
        total = each_df.shape[0]
        not_map_percent = round(not_mapped / total, 2)
        map_percent = round(mapped / total, 2)
        print(f'{each},{total},{mapped},{map_percent*100},{not_mapped},{not_map_percent*100}')
    print("finished")


if __name__ == '__main__':
    stats_data()
