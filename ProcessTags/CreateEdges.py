import json, csv, os, glob, pandas as pd
from collections import Counter
from itertools import combinations

# creates tuples of wordpairs
def createEdges(df):
    lol = []
    for line in df: 
        if type(line) == float:
            continue
        lol.append(line.split(', '))

    perm = []
    for row in lol:
        a = (list(combinations(row,2)))
        [perm.append(tuples) for tuples in a]
    
    res = [tuple(sorted(k)) for k in perm]
   
    return res

# create one big df from every document in path
#path = ('../zdf_data/cleaned/csv/03_09')

#big_frame = pd.concat([pd.read_csv(f, sep = ';') for f in glob.glob(path + "/*.csv")],
#                      ignore_index=True)

filename = '03_09_zdf_dokumentation_zdfzoom'
file = pd.read_csv('../zdf_data/cleaned/csv/03_09/' + filename + '.csv', encoding='utf-8', delimiter=';')

#big_frame = pd.DataFrame(file)

# save editorialTags in variable
editorialTags = file['editorialTags']
allTags = file['allTags']

# create Edges     
data = createEdges(editorialTags)
data2 = createEdges(allTags)

# Count all tuples and save counts to variables
words = list(Counter(data).keys())
counts = list(Counter(data).values())

words2 = list(Counter(data2).keys())
counts2 = list(Counter(data2).values())

# create DataFrame and save to file
df = pd.DataFrame(words, columns=['Source', 'Target'])
de = pd.DataFrame(words2, columns=['Source', 'Target'])

df['Weight'] = counts
de['Weight2'] = counts2


#df.to_csv('../zdf_data/cleaned/csv/tags/editorialTags_combi_edges.csv', encoding='utf-8-sig', sep=';')

n1 = df.sort_values(by=['Weight'], ascending=False)
n2 = de.sort_values(by=['Weight2'], ascending=False)

print(n1.head(5))
print('___________________________________________________________________________________')
print(n2.head(5))