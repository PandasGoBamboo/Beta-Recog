import json, csv, pandas as pd 
from collections import Counter

in_dir = '../zdf_data/cleaned/csv/03_09/'
out_dir = '../zdf_data/cleaned/csv/tags/'
filename = '03_09_zdf_dokumentation_terra-x'

# read csv-file
file = pd.read_csv(in_dir + filename + '.csv', encoding='utf-8', delimiter=';')

def saveTags(colum):
    all = []
    for word in colum:
        # Jede Spalte
        split = str(word).split(',')
        all.append((len(split)))
    return all 

et = file['editorialTags']
# save allTags in variable
at = file['allTags']

et_list = saveTags(et)
at_list = saveTags(at)

df = pd.DataFrame({'Counts EDI': et_list})
de = pd.DataFrame({'Counts ALL': at_list})


print(df['Counts EDI'].mean())
print('-------------------')
print(df['Counts EDI'].median())
print('-------------------')
print(de['Counts ALL'].mean())
print('-------------------')
print(de['Counts ALL'].median())
print('-------------------')