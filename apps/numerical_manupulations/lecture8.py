import numpy as np

int_list = [1, 2, 3, 4, 5]
np_array = np.array([int_list, [i * i for i in int_list]])
print(np_array)
print(np_array/2)
print(np_array-np_array)
