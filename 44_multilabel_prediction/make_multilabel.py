from sklearn.datasets import make_multilabel_classification
from lightgbm import LGBMClassifier as lgbm
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
import numpy as np 

X, Y = make_multilabel_classification(
    n_classes=4, 
	n_labels=2, 
	n_samples = 1000,
	allow_unlabeled=True, 
	random_state=6,
)

X_test, X_train, y_test, y_train = train_test_split(X,Y,test_size=0.3)

clf = OneVsRestClassifier(lgbm())
clf.fit(X_train,y_train)

pred = clf.predict_proba(X_test)

print(pred)


