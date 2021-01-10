import pandas as pd

path = r"C:\Users\chara\Downloads\311_neighborhood.csv"

df_311 = pd.read_csv(path)
df_311 = df_311[df_311['DAYS TO CLOSE'].notna()]
group_df = df_311.groupby(by=['nbh_id'])['DAYS TO CLOSE'].mean().reset_index()
group_df.to_csv("group.csv", index=False, header=True)
