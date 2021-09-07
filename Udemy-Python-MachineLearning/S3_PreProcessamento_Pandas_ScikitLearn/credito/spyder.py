# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:02:48 2020

@author: vitor
"""
import pandas as pd
df = pd.read_csv('credit-data.csv', sep=',')
pd.__version__

df.describe()