"""This method calculates bmi"""

import numpy as np

height = [1.5, 1.6, 1.8, 1.75, 1.55, 1.90, 1.7, 1.85, 1.8]
weight = [230, 150, 240, 250, 175, 132, 180, 210, 205]

lbs_to_kg = 0.453592

np_height = np.array(height)
np_weight = np.array(weight)
np_weight_kg = np_weight * lbs_to_kg

np_bmi_raw = np_weight_kg / np_height ** 2
np_bmi = np.round(np_bmi_raw, 2)

print('BMI =>', np_bmi)
print('BMI >30 =>', np_bmi[np_bmi > 30])
print('One BMI =>', np_bmi[1])
print('Three BMIs =>', np_bmi[1:4])

# watchmedo log --patterns="*.py;*.txt" --ignore-directories --recursive .
# watchmedo shell-command --patterns="*.py" command='echo "${watch_src_path}"' .
