import numpy as np

my_list1 = [1, 2, 3, 4]
my_list2 = [11, 22, 33, 44]

np_array1 = np.array(my_list1)

print(np_array1.dtype)

my_lists = [my_list1, my_list2]

print(np_array1)
print(np_array1.shape)

np_array2 = np.array(my_lists)

print(np_array2.shape)

print(np.zeros([2, 4]).astype(int))

print(np.ones([2, 4]).astype(int))

print(np.empty([2, 4]).astype(int))

np_arange = np.arange(5, 50, 2)

print(np_arange.shape)
