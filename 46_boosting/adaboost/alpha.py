
from math import log
import numpy as np

error = 0.3

multiplier_weight = np.sqrt((1-error)/error)
multiplier_weight2 = np.sqrt(error/(1-error))

print(multiplier_weight)
print(multiplier_weight2)
