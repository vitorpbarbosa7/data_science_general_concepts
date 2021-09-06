    import pandas as pd 
    
    base = pd.read_csv('credit-data.csv')

#Filtro muito louco com atualização e impute:
base.loc[base.age <0, 'age'] = 40.92


#Receita e Idade
plt.scatter(base.iloc[:,1], base.iloc[:,2])
plt.xlabel('Receita')
plt.ylabel('Idade')

#Receita e empréstimo
plt.scatter(base.iloc[:,1], base.iloc[:,3])
plt.xlabel('Receita')
plt.ylabel('Empréstimos')

#Idade e empréstimo
plt.scatter(base.iloc[:,2], base.iloc[:,3])
plt.xlabel('Idade')
plt.ylabel('Empréstimos')

#Utilizando outra base:
base_census = pd.read_csv('census.csv')

#Idade e peso final
plt.scatter(base_census.iloc[:,0], base_census.iloc[:,2])
plt.xlabel('Idade')
plt.ylabel('Peso final (Importância da pessoa na base do censo)')Py