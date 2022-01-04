import pandas as pd

base = pd.read_csv('credit-data.csv')
base.dropna()