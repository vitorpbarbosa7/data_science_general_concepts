import h5py

f = h5py.File('cnn.h5', 'r')

for keys, values in f.items():
	print(keys)
	print(values)


data = list(f['model_weights'])

import pandas as pd

df = pd.DataFrame(data)

df.head()

df

print(df)