import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from lightgbm import LGBMClassifier as lgbm

X = np.array([
	[10,10],
	[8,10],
	[-5,5.5],
	[-5.4,5.5],
	[-20,20],
	[-15,-20]
])

# dense matrix
y = np.array([[1,0,0], [1,0,1], [1,1,0], [0,1,0], [0,0,1], [0,1,1]])

clf = OneVsRestClassifier(estimator = SVC()).fit(X,y)

lgbm_clf = OneVsRestClassifier(estimator = lgbm()).fit(X,y)

X_test = [[-19,-20], [9,9], [-5,5]]
prediction = clf.predict(X_test)
lgbm_prediction = lgbm_clf.predict_proba(X_test)

print(prediction)
print(lgbm_prediction)

