import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../zdf_data/cleaned/csv/analysis/bar_test.csv', encoding='utf-8', sep=';')

label = df['Label']
counts = df['Counts']

# x axis Labels
first = label[0]
middle = label[304]
last = label[809]

plt.bar(x= label,height= counts, label=None)
plt.xticks([first, middle, last], [first, middle, last])
plt.savefig('../zdf_data/cleaned/csv/analysis/bar_test.png')
plt.show()

