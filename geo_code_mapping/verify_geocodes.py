import pandas as pd
import json

new_json = "/home/charan/DATA/311_Data/Boundary/address0.json"
path = "/home/charan/DATA/311_Data/Boundary/311_call_data.csv"
path1 = "/home/charan/DATA/311_Data/Boundary/311_call_data_new.csv"


def setup_process():
    with open(new_json, 'r') as f:
        geo_codes = json.load(f)
        f.close()
    for each in list(geo_codes.keys()):
        list_address = geo_codes[each]
        trimmed_list = [add.split(",")[0] for add in list_address]
        geo_codes[each] = trimmed_list
    return geo_codes


geo_codes = setup_process()


def apply_tag_address(input_record):
    input_str = '{},{}'.format(input_record['LATITUDE'], input_record['LONGITUDE'])
    list_add = geo_codes[input_str]
    for each in list_add:
        if str(input_record['STREET ADDRESS']) in str(each) or str(each) in str(input_record['STREET ADDRESS']):
            return 1
    return 0


def tag_address():
    data = pd.read_csv(path)
    data['tag'] = data.apply(lambda x: apply_tag_address(x), axis=1)
    data.to_csv(path1, header=True, index=False)
    print("finished")


def tag_address1():
    data = pd.read_csv(path1)
    grouped_df = data.groupby(by=['LATITUDE', 'LONGITUDE'])['CASE ID'].count().reset_index(name="count")
    print("finished")

if __name__ == '__main__':
    tag_address1()
