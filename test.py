"""
Trying out numpy features
"""

import numpy as np

a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(a)
a = np.array(a)
print(a)
x = np.arange(20)
y = np.arange(10)
print(x)
print(y)
print(np.size(x))
print(np.size(y))

x = x.reshape(4, 5)
y = y.reshape(10, 1)

print(y)
x = np.linspace(0, 2, 11)
print(x)
print(y * x)
print(x * y)
