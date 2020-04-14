import pandas as pd

csv_file = '/home/charan/Documents/workspaces/python_workspaces/python_practice_workspace/pytorch_train/image.csv'

csv_file = pd.read_csv(csv_file, header=None)
list_values = csv_file[0].values.tolist()

for item in range(7):
    label = list_values[item]
    print(label)
