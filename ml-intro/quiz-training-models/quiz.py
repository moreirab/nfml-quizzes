import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

# Read the data
data = pd.read_csv('data.csv')

# Split the data into X and y
X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

# import statements for the classification algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# TODO: Pick an algorithm from the list:
# - Logistic Regression
# - Decision Trees
# - Support Vector Machines
# Define a classifier (bonus: Specify some parameters!)
# and use it to fit the data

#classifier = LogisticRegression()
#classifier = GradientBoostingClassifier()
classifier = SVC()

# tanto o GradientBoostingClassifier quanto o SVC se ajustaram precisamente em relação aos dados;
# LogisticRegression não funcionou neste caso.
classifier.fit(X, y)