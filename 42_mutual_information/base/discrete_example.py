import numpy as np
from math import log
from numpy import array as ar

from sklearn.feature_selection import mutual_info_classif

X = ar([2,2,2,3,3])
y = ar([1,1,1,0,1])

payzero = 1E-12
pbyzero = 1/5

payone = 3/5
pbyone = 1/5

pyzero = 1/5
pyone = 4/5

pa = 3/5
pb = 2/5

b = payzero*log(payzero/(pa*pyzero))
d = pbyzero*log(pbyzero/(pb*pyzero))

c = pbyone*log(pbyone/(pb*pyone))
a = payone*log(payone/(pa*pyone))

Ixy = a + b + c + d
print(Ixy)


mic = mutual_info_classif(X.reshape(-1,1),y, discrete_features = True)

print(mic)
