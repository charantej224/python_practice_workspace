import pandas as pd
import os

root_dir = "/home/charan/DATA/311_Data"
block_data = os.path.join(root_dir, "311_VIZ_DESCRIPTION_PARENT_CLASS.csv")
geo_code = os.path.join(root_dir, "GEO_DUPLICATES.csv")
count_df = os.path.join(root_dir, "COUNT_DUPS.csv")
neihg_df = "/home/charan/Downloads/311_call_2007_2020_Neighborhood.csv"


def data_error_geo_code():
    list_count_df = []
    list_df = []
    block_df = pd.read_csv(block_data)
    grouped = block_df[['CASE ID', 'LATITUDE', 'LONGITUDE']].groupby(by=['LATITUDE', 'LONGITUDE'])[
        'CASE ID'].count().reset_index()
    grouped = grouped[grouped['CASE ID'] > 1]
    grouped.rename(columns={"CASE ID": "COUNT"}, inplace=True)
    for index, row in grouped.iterrows():
        print(f"processing {index}")
        each_df = block_df[block_df.LATITUDE == row['LATITUDE']]
        each_df = each_df[each_df.LONGITUDE == row['LONGITUDE']]
        list_address = list(each_df['STREET ADDRESS'].unique())
        for each in list_address:
            count = each_df[each_df['STREET ADDRESS'] == each].shape[0]
            list_count_df.append(
                {'LATITUDE': row['LATITUDE'], 'LONGITUDE': row['LONGITUDE'], "TOTAL_COUNT": row['COUNT'],
                 'ADRESS_COUNT': count, 'ADRESS': each})
        # list_df.append(each_df)
        # print(row['COUNT'])
    # duplicated_geo = pd.concat(list_df)
    # duplicated_geo.to_csv(geo_code, index=False)
    df_count = pd.DataFrame(list_count_df)
    df_count.to_csv(count_df, index=False)
    print("finished")


def block_analysis():
    block_df = pd.read_csv(block_data)
    not_block_df = block_df[block_df.block_id.notna()]
    list_block = list(not_block_df.NEIGHBORHOOD.unique())
    for each in list_block:
        each_df = not_block_df[not_block_df.NEIGHBORHOOD == each]
        print(f'"{each}"-{each_df.shape[0]}')


def neighborhood():
    block_df = pd.read_csv(neihg_df)
    print("finished")


if __name__ == '__main__':
    block_analysis()
