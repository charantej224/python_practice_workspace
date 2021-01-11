import pandas as pd

visible_path = "/home/charan/DATA/311_Data/311_NEIGH_VIS_NONVIS_v1.csv"

data_visible = pd.read_csv(visible_path)
print(data_visible.shape)
