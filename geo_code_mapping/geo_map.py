import pandas as pd
import json
import requests


def prepare_records():
    lat_json = "/home/charan/DATA/311_Data/Boundary/lat.json"
    path = "/home/charan/DATA/311_Data/Boundary/311_call_data.csv"
    data = pd.read_csv(path)
    group_by_df = data.groupby(by=['LATITUDE', 'LONGITUDE'])['CASE ID'].count().reset_index(name='count')
    dict_records = group_by_df.drop('count', axis=1).to_dict('records')
    with open(lat_json, 'w') as f:
        json.dump(dict_records, f, indent=2)
        f.close()
    print("finished")


def get_address(latitude, longitude):
    key = "{},{}".format(latitude, longitude)
    list_formatted = []
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyABx4svgWT--wKRhDDClID__N4qtApptR8"
    return_val = requests.get(url.format(latitude, longitude))
    for each in json.loads(return_val.text)['results']:
        list_formatted.append(each['formatted_address'])
    return key, list_formatted


def process_address():
    new_json = "/home/charan/DATA/311_Data/Boundary/address.json"
    map_address = {}
    lat_json = "/home/charan/DATA/311_Data/Boundary/lat.json"
    with open(lat_json, 'r') as f:
        records = json.load(f)
        f.close()
    for each in records:
        key, value = get_address(each['LATITUDE'], each['LONGITUDE'])
        map_address[key] = value
    with open(new_json, 'w') as f:
        json.dump(map_address, f, indent=2)
        f.close()


if __name__ == '__main__':
    process_address()
