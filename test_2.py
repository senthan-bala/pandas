"""
Trying out pandas features
"""

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})

# Find index of element in column 'B'
print(df[df['B'] == 30].index[0])
