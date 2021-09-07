import pandas as pd

base = pd.read_csv('credit-data.csv')
base = base.dropna()

#Retirar os valores negativos
base = base[base['age']>=0]

import matplotlib.pyplot as plt

#ShowFliers controla se mostra ou não mostra os outliers
plt.boxplot(base.iloc[:,2], showfliers = True)

#Outra maneira de realizar o filtro
outliers_age = base[(base.age < 0)]

#Para o loan
plt.boxplot(base.iloc[:,3])

outliers_loan = base[(base.loan)]

loan_sortby = base.sort_values(by=['loan'])
