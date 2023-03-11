from numpy import array as ar
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor

def objective(x, noise = 0.1):
	noise = np.random.normal(loc=0, scale = noise)
	multimodal = (x**2 * np.sin(5*np.pi*x)**6) + noise
	return multimodal

# The grid-base:
X = np.arange(0,1,0.01)
multimodal = objective(X)

def plot_one(X,multimodal):
	plt.scatter(x = X, y = multimoda)
	plt.show()
# evaluate without noise
y = [objective(x,0) for x in X]
y_noise = [objective(x) for x in X]
#plot_one(X,y)
#plot_one(X,y_noise)

argument_index_maximizes_function = np.argmax(y)
idx = argument_index_maximizes_function
print(f'Optima value is ({X[idx]},{y[idx]})')

#surrogate or approximation for the objective function
# since we do not have its shape, we will use some way to find the intermediate points
# Gaussian Process Regressor
model = GaussianProcessRegressor()
X = X.reshape(-1,1)
# fit the model
model.fit(X, y)
def surrogate(model, X):
	# catch any warning generated when making a prediction
	#with catch_warnings():
	# ignore generated warnings
	#simplefilter("ignore")
	return model.predict(X, return_std=True)

y_hat = surrogate(model, X)

def plot(X, y, model):
	
	# scatter plot of inputs and real objective function
	plt.scatter(X, y)

	# line plot of surrogate function across domain
	Xsamples = np.asarray(np.arange(0, 1, 0.001))
	Xsamples = Xsamples.reshape(len(Xsamples), 1)
	ysamples, _ = surrogate(model, Xsamples)
	plt.plot(Xsamples, ysamples)
	# show the plot
	plt.show()

# Amostrar do dominio esparso com disturbio
X = np.andom(100)


# otimizar a funcao de aquisicao
def otimizar_funcao_aquisicao(X, y, model):
	# random search, gerar amostras aleatórias
	# no optuna essa distribuicao já não está disponível do range que passamos?

	Xsamples = np.random(100)

	Xsamples = Xsamples.reshape(len(Xsamples), 1)

	# Calcular a funcao de aquisicao 
	scores = funcao_aquisicao(X, Xsamples, model)

	# localizar o indice com maior socre da funcao de aquisicao
	idx = np.argmax(scores)

	# Retorne a partir da amostra aleatória, qual dos valores que maximiza a funcao de aquisicao
	return Xsamples[idx, 0]





