from pandas import Series, DataFrame
import pandas as pd

a_series = Series([2, 3, 4, 5, 6])
print(a_series)
print(a_series.index)
print(a_series.values)

print(a_series[a_series > 4])
print(a_series[2])

b_series = Series([2, 3, 4, 5, 6], index=['two', 'three', 'four', 'five', 'six'])
print(b_series['two'])
dick_head = b_series.to_dict()
print(dick_head['two'])

data_frame = pd.read_csv('input_file.txt')
print(data_frame)
print(DataFrame(data_frame, columns=['team', 'win']))
print(data_frame.iloc(1))

c_series = Series([5, 6, 7, 8, 9], index=['five', 'six', 'seven', 'eight', 'nine'])
c_index = c_series.index
print(c_index[2])
print(c_index[4:])
# c_index[4] = 'NINE' -- index immutable
