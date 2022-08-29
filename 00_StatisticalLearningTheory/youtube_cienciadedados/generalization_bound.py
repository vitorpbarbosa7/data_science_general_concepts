import numpy as np
import matplotlib.pyplot as plt 

amostras = range(1000,10000,1)

riscos_empiricos = [0.01,0.1]
delta = 0.05

power = 4
risco_esperado = []
risco_esperado.append([riscos_empiricos[0] + np.sqrt((4/n)*(np.log(2*(n**(power))) - np.log(delta))) for n in amostras])
risco_esperado.append([riscos_empiricos[1] + np.sqrt((4/n)*(np.log(2*(n)) - np.log(delta))) for n in amostras])

classifier = [f'n^{power}','n']
for i, risco_empirico in enumerate(riscos_empiricos):
	plt.scatter(x = amostras, y = risco_esperado[i], label = str(risco_empirico)+' '+classifier[i])

plt.legend()
plt.show()

