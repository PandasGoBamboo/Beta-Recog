import json, csv, pandas as pd 
from collections import Counter
import glob
in_dir = '../zdf_data/cleaned/csv/03_09/'
out_dir = '../zdf_data/cleaned/csv/tags/'
filen = '03_09_zdf_dokumentation_'
#name = '37-grad'
#name = 'der-haustier-check'
#name = 'dokumentation-sonstige'
#name = 'planet-e'
#name = 'terra-x'
#name = 'zdf-history'
#name = 'zdfinfo-doku'
#name = 'zdf-reportage'
#name = 'zdfzeit'
name = 'zdfzoom'

in_path = '../zdf_data/cleaned/csv/03_09/'

# Einstellung für alle Dokumente zusammen.
big_frame = pd.concat([pd.read_csv(f, sep=';') for f in glob.glob(in_path + "/*.csv")],
                      ignore_index=True)

# read csv-file
file = pd.read_csv(in_dir + filen + name + '.csv', encoding='utf-8', delimiter=';')

def saveTags(colum):
    all = []
    for word in colum:
        split = str(word).split(',')
        for t in split:
            all.append(t.strip())
    return all 

#save editorialTags in variable
et = big_frame['editorialTags']
# save allTags in variable
at = big_frame['allTags']


et_list = saveTags(et)
at_list = saveTags(at)



# count uniq words and save words and counts in to lists
words_et = list(Counter(et_list).keys())
counts_et = list(Counter(et_list).values())

words_at = list(Counter(at_list).keys())
counts_at = list(Counter(at_list).values())

df = pd.DataFrame({'Label EDI': words_et, 'Counts EDI': counts_et})

de = pd.DataFrame({'Label ALL': words_at, 'Counts ALL': counts_at})


sorted = df.sort_values(by=['Counts EDI'], ascending=False)
sorted2 = de.sort_values(by=['Counts ALL'], ascending=False)



# create variable category with length of words
#category = []
#[category.append('zdfzoom') for filename in range(len(words))]

# df.to_csv(out_dir + filename + '_alltags.csv', encoding='utf-8-sig', sep=';', mode='a')

def saveTags2(colum):
    all = []
    for word in colum:
        # Jede Spalte
        split = str(word).split(',')
        all.append((len(split)))
    return all 


et = big_frame['editorialTags']
# save allTags in variable
at = big_frame['allTags']

et_list2 = saveTags2(et)
at_list2 = saveTags2(at)

df2 = pd.DataFrame({'Counts EDI': et_list2})
de2 = pd.DataFrame({'Counts ALL': at_list2})



print("Count EDITAGS: ", len(et_list))
print("Unique EDI ", len(df))
print("Mittel: ", df2['Counts EDI'].mean())
print("Median: ", df2['Counts EDI'].median())
print('-------------------')
print("Count ALLTAGS: ", len(at_list))
print("Unique ALL ", len(de))
print("Mittel: ", de2['Counts ALL'].mean())
print("Median: ", de2['Counts ALL'].median())
print(sorted.head(10))
print('##########################')
print(sorted2.head(10))