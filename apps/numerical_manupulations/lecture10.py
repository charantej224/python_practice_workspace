import numpy as np

reshaped = np.zeros(50).reshape((10, 5))
print(reshaped)
reshaped[1] = 1
print(reshaped)
print(reshaped.T)
