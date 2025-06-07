'This method calculates area for given length & width'

import numpy as np

col1 = np.round(np.random.normal(200, 20, 11), 2)
col2 = np.round(np.random.normal(20, 2, 11), 2)
matrix = np.column_stack((col1, col2))
print('Matrix of random numbers =>', matrix)
print('Mean on col1 =>', np.mean(col1))
print('Median on col1 =>', np.median(col1))

std = np.std(col1)
print('Std Dev on col1 => ' + str(std))

correlation = np.corrcoef(col1, col2)
print('Correlation on col1 => ' + str(correlation))
