# https://www.youtube.com/watch?v=eJIp_mgVLwE

import numpy as np
from numpy import array as ar
import pandas as pd

popcorn = [1,1,1,0,0]
height = [1.77,1.32,1.81,1.56,1.64]
target = [1,1,1,0,1]

probs = pd.crosstab(popcorn, target, normalize = 'index')
print(probs)


