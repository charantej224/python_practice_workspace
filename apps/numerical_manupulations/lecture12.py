import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01)
dx, dy = np.meshgrid(points, points)
print("------------")
print(dx)
print("------------")
print(dy)
print("------------")
dz = np.add(np.sin(dx), np.sin(dy))

print(dz)
plt.imshow(dz)
plt.show()

A = np.array([1, 2, 3, 4])
B = np.array([1000, 2000, 3000, 4000])
condition = np.array([True, True, False, False])

print([(a_val if cond else b_val) for a_val, b_val, cond in zip(A, B, condition)])
print(np.where(condition, A, B))
print(dz)
print(np.where(dz < 0, 0, dz))
