import numpy as np

arr = np.arange(0, 11)

print(arr)

print(arr[0:1])

print(arr[:3])
print(arr[1:])

array_2d = np.array(([0, 1, 2], [2, 3, 4], [5, 6, 7]))
print(array_2d[0:1])
print(array_2d[1][1])

print(array_2d[:2, :2])

zeros_array = np.zeros((10, 10))

zeros_array = zeros_array.astype(int)
print(zeros_array.shape)