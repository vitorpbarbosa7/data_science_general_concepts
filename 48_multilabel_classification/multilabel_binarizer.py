from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()

array = [('A','B'), ('C'), ('A','D')]

output = mlb.fit_transform(array)
print(output)
print(mlb.classes_)
