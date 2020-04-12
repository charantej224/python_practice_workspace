import pandas as pd

input_file = 'regular.csv'
input_file_map = 'regular_map.csv'
output_file_csv = 'regular_output.csv'

regular_csv = open(input_file, 'r')
regular_map = open(input_file_map, 'r')

regular_map_dict = {}
map_data_frame = pd.read_csv(regular_map)

for _, row in map_data_frame.iterrows():
    regular_map_dict[row.label] = row.label + ' - ' + str(row.map_score)

prediction_data_frame = pd.read_csv(input_file)
index_list = prediction_data_frame['label'][0:].tolist()
prediction_data_frame = prediction_data_frame.drop(['label'], axis=1)
prediction_data_frame.index = index_list

row_list = []
for i in regular_map_dict:
    for j in regular_map_dict:
        if i != j and prediction_data_frame[i][j] > 0:
            row_list.append((regular_map_dict[i], regular_map_dict[j], prediction_data_frame[i][j]))

print(row_list)
final_df = pd.DataFrame(row_list, columns=['Ground_Truth', 'Prediction', 'Occurences'])
print(final_df)
final_df.to_csv(output_file_csv, index=False)
