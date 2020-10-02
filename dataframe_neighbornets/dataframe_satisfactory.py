path = "/home/charan/Downloads/Citizen_Satisfaction_Survey_Results_Previous_Years_To_Present.csv"

import pandas as pd

satisfaction_df = pd.read_csv(path)
satisfaction_df = satisfaction_df.fillna(0)
satisfaction_df['Year'] = satisfaction_df['Year'].apply(lambda x: x.replace("FY", ""))

satisfaction_df = satisfaction_df.drop(columns=["Year (Date)"])

column_data = satisfaction_df.columns

parent_map = {}

for _, row in satisfaction_df.iterrows():
    year = ""
    list_dict = []
    for each in column_data:
        if each == 'Year':
            year = row[each]
            continue
        else:
            dict_val = {
                "category_type": each,
                "satisfaction_index": row[each]
            }
            list_dict.append(dict_val)
        parent_map[year] = list_dict

final_list = []

for key in parent_map.keys():
    for each in parent_map[key]:
        each['Year'] = key
        final_list.append(each)

df = pd.DataFrame(final_list)
df["City"] = 'Kansas City'
df.to_csv("kgraph_satisfactory_index.csv", index=False, header=True)
