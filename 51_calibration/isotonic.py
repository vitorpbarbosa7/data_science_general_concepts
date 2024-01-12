import pickle
from sklearn.isotonic import IsotonicRegression

with open('probs.pickle', 'rb') as f:
    probs = pickle.load(f)

y_train = probs['train_scores']
y_test = probs['test_scores']
y_train = probs['y_train']
y_test = probs['y_test']


iso = IsotonicRegression()

iso_reg = IsotonicRegression().fit(X, y)
iso_reg.predict([.1, .2])
