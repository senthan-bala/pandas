"""This method calculates area for given length & width"""

import numpy as np

# from numpy import array

LENGTH = 100
WIDTH = 34.5
AREA = LENGTH * WIDTH

print("Area", AREA, sep=" = ", end="; ")

a_1d = [[0, 1, 2], [12, 13, 14], [22, 23, 24], [32, 33, 34]]
np_a_1d = np.array(a_1d)
print("Array shape =>", np_a_1d.shape)
print("Specific element =>", np_a_1d[1, 0])
print("Sublist =>", np_a_1d[:, 1:3])

a_2d = [[4, 5, 8, 11, 12], [8, 7, 5, 4, 7], [10, 5, 4, 8, 5], [8, 6, 4, 7, 6]]
np_a_2d = np.array(a_2d)
b_2d = [
    [14, 15, 18, 21, 22],
    [18, 17, 15, 14, 17],
    [20, 15, 14, 18, 15],
    [18, 16, 14, 17, 16],
]
np_b_2d = np.array(b_2d)

print("Shape =>", np_a_2d.shape)
print("Subset =>", np_a_2d[1, :3])
print("Subset =>", np_a_2d[3, :])
print("Subset =>", np_a_2d[2:4, 1:4])

c_2d = a_2d + b_2d
np_c_2d = np_a_2d + np_b_2d
print("Addition - Regular array =>", c_2d)
print("Addition - np array =>", np_c_2d)
