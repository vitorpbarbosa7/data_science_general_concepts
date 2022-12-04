import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_classif
import seaborn as sns
import matplotlib.pyplot as plt

def fg(w = 10, h = 7, dpi = 200):
    plt.rcParams['figure.figsize'] = (w,h)
    plt.rcParams['figure.dpi'] = dpi

df = pd.read_csv('data/glass.csv', sep = ',')

df.columns = [f'x_{i}' for i in range(df.shape[1]-1)] + ['class']

X_train = df.drop('class', 1)
y_train = df['class']
X_train = X_train.astype(float)

sns.countplot(X_train.isna().sum()/X_train.shape[0])
plt.show()

mi = mutual_info_classif(X_train, y_train)

cols = X_train.columns
values = np.round(mi.view(),4)
dicti = dict(zip(cols,values))

_plot = pd.DataFrame.from_dict(
    data = dict(sorted(dicti.items(), 
    key=lambda item: item[1])), 
    orient = 'index'
    )

_plot = _plot.reset_index().rename(
    columns = {'index':'features',0:'mutual_information'}
    ).sort_values(by = 'mutual_information', ascending =  False)
_plot

_show = 10
values = _plot.mutual_information[:_show]
fg(w = 7, h = _show*0.35)
sns.barplot(y = _plot.features[:_show], x = values, hue = values, orient = 'h')
plt.show()
