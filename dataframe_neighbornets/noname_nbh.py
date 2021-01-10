import pandas as pd
import json

df_path = r"C:\Users\chara\Documents\Data\no_name\0_neighborhood.csv"
df_path_new = r"C:\Users\chara\Documents\Data\no_name\0_neighborhood_obj.csv"
file_path = r"C:\Users\chara\Downloads\Kansas City Neighborhood Boundaries.geojson"

df_values = pd.read_csv(df_path)
with open(file_path, 'r') as f:
    geo_json = json.load(f)["features"]


def map_neighborhood(input):
    lattitude, longtitude = input['LATITUDE'], input['LONGITUDE']
    for each in geo_json:
        right_top, right_bottom = False, False
        left_top, left_bottom = False, False
        list_geo_points = each['geometry']['coordinates'][0][0]
        object_id = each["properties"]["objectid"]
        print("each record")
        for each_point in list_geo_points:
            if lattitude < each_point[1] and longtitude < each_point[0]:
                right_top = True
            if lattitude < each_point[1] and longtitude > each_point[0]:
                right_bottom = True
            if lattitude > each_point[1] and longtitude > each_point[0]:
                left_bottom = True
            if lattitude > each_point[1] and longtitude < each_point[0]:
                left_top = True
            if right_top and right_bottom and left_top and left_bottom:
                print(object_id)
                return object_id


def process_no_name():
    df_values["obj_id"] = df_values.apply(map_neighborhood, axis=1)
    df_values.to_csv(df_path_new, header=True, index=False)


def object_id_values():
    ob_df = pd.read_csv(df_path_new)
    list_obj = sorted(list(ob_df.obj_id.unique()))
    ob_df["nbh_name"] = "no-name"
    for each in list_obj:
        each_df = ob_df[ob_df.obj_id == each]
        each_path = r"C:\Users\chara\Documents\Data\no_name\{}_no_name_neighborhood_obj.csv".format(each)
        each_df.to_csv(each_path, index=False, header=True)
        print(f'object id {each} - shape {each_df.shape}')


if __name__ == '__main__':
    dict_geo = {
        "LATITUDE": 39.085188,
        "LONGITUDE": -94.562637
    }
    map_neighborhood(dict_geo)
