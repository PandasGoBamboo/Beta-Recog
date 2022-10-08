import pandas as pd
import pickle

file = 'C:/Users/tschu/Desktop/BETA-RECOG/stemmed_raw_data.pkl'

print('Ich roedel......')

data = pd.read_pickle(file)

g = data.groupby('pform')
b = g.apply(lambda x: x.sample(g.size().min()).reset_index(drop=True))

b.to_pickle('same_sample_size.pkl')
print('done')