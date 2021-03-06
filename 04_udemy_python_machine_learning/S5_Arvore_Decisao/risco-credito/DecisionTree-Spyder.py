import pandas as pd

base = pd.read_csv('risco-credito.csv')
previsores = base.iloc[:,0:4].values
classe = base.iloc[:,4].values
                  
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])
                 
from sklearn.tree import DecisionTreeClassifier, export
classificador = DecisionTreeClassifier(criterion = 'entropy')    
classificador.fit(previsores, classe)


export.export_graphviz(classificador, out_file = 'arvore.dot',
                       feature_names = ['historia', 'dívida', 'garantias', 'renda'],
                       class_names= ['alto', 'moderado', 'baixo'],
                       filled=True,
                       leaves_parallel=True)


resultado = classificador.predict([[0,0,1,2], [3,0,0,0]])
print(classificador.classes_)