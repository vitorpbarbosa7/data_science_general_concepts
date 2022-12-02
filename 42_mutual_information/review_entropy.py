import matplotlib.pyplot as plt
import numpy as np
from math import log2
from typing import Tuple, Union
from functools import reduce

def fg(w = 10, h = 7, dpi = 200):
    plt.rcParams['figure.figsize'] = (w,h)
    plt.rcParams['figure.dpi'] = dpi

def entropy(*args) -> float:
    return reduce(lambda x, y: x*log2(1/x) + y*log2(1/y), *args)

## Balanced case

entropy((0.25,0.25,0.25,0.25))

probs = tuple([0.2]*5)
entropy(probs)

## Unbalanced case

probs = (0.2,0.8)
entropy(probs)

probs = np.arange(0.01,0.99,0.01)
tupleprobs = tuple(zip(probs, 1-probs))

fg(8,4)
plt.scatter(x = probs, y = [entropy(prob) for prob in tupleprobs])
plt.xlabel('Probabilities')
plt.ylabel('Entropy')
plt.show()

## Machine Learning Mastery
# https://machinelearningmastery.com/information-gain-and-mutual-information/
# calculate the entropy for a dataset
# proportion of examples in each class
class0 = 10/100
class1 = 90/100
entropy = (class0 * log2(1/class0) + class1 * log2(1/class1))
print('entropy: %.3f bits' % entropy)

# Mutual Information at last

#- Redução na incerteza de uma variável, dada o conhecimento sobre outra variável, 

#- Em outros termos, qual a redução na entropia de uma variável aleatória, dado o conhecimento sobre a distribuição de probabilidade de outra variável

#- Resultado em bits
