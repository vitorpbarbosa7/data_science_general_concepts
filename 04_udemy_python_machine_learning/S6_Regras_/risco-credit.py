import Orange

base = Orange.data.Table('risco-credito.csv')

base.domain

cn2_learner = Orange.classification.rules.CN2Learner()
classificador = cn2_learner(base)

#Vamos imprimir as regras agora então 
for regras in classificador.rule_list:
    print(regras)
    
resultado = classificador([['boa', 'alta', 'nenhuma', 'acima_35'],
                           ['ruim', 'alta', 'adequada', '0_15']])
    
resultado

for i in resultado:
    print(base.domain.class_var.values[i])