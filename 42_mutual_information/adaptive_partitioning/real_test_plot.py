import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.feature_selection import mutual_info_classif
from teaspoon.parameter_selection.MI_delay import MI_DV

df = pd.read_csv('../data/archive/aps_failure_training_set.txt', sep = ',')
test = pd.read_csv('../data/archive/aps_failure_test_set.txt', sep = ',')

test = test.replace('na',np.nan)
test = test.dropna()

X_test = test.drop('class', axis = 1)
y_test = test['class']

df = df.replace('na',np.nan)
df = df.dropna()

X_train = df.drop('class', 1)
y_train = df['class']
X_train = X_train.astype(float)

x_array = X_train.iloc[:,3].values
y_train = y_train.values


MI_DV(X_train, y_train)




