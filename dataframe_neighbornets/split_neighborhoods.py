import pandas as pd
import logging
import re

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # or whatever
handler = logging.FileHandler(r"C:\Users\chara\Documents\Data\all_neigh\meta_data.log", 'w', 'utf-8')  # or whatever
handler.setFormatter(logging.Formatter('%(name)s %(message)s'))  # or whatever
root_logger.addHandler(handler)

df_path = r"C:\Users\chara\Downloads\311_neighborhood.csv"
df_path = r"C:\Users\chara\Downloads\311_neighborhood (1).csv"

whole_df = pd.read_csv(df_path)
print(whole_df.shape)
list_neighborhoods = list(whole_df.nbh_id.unique())
whole_df.nbh_name = whole_df.nbh_name.fillna("no-name")
df_2020 = whole_df[whole_df['CREATION YEAR'] == 2020]
sum = 0
for each in list_neighborhoods:
    each_df = whole_df[whole_df.nbh_id == each]
    names_list = list(each_df.nbh_name.unique())
    names_list = [re.sub('[^A-Za-z0-9]+', '-', str(each)) for each in names_list]
    neigh = "_".join(names_list)
    path = r'C:\Users\chara\Documents\Data\all_neigh\{}_{}.csv'.format(each, neigh)
    each_df.to_csv(path, header=True, index=False)
    logging.debug(f'{each} - {each_df.shape}')
    sum += each_df.shape[0]

print(sum)
