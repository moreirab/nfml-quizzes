import pandas as pd
import numpy as np

# TODO: Use pandas to read the '2_class_data.csv' file, and store it in a variable
# called 'data'.
in_file = '2_class_data.csv'
data = pd.read_csv(in_file)

# TODO: Separate the features and the labels into arrays called X and y
X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])