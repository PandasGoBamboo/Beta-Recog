import json, csv, pandas as pd 
from collections import Counter
import os
import glob

# save all tags in each row in one array
def getAllTags(input):
    all = []
    for word in input:
        if type(word) == float :
            continue
        split = str(word).split(', ')
        for t in split:
            all.append(t.strip())  #.lower() 
    return all

path = ('../zdf_data/cleaned/csv/03_09')

# create one big df from every document in path
big_frame = pd.concat([pd.read_csv(f, sep=';') for f in glob.glob(path + "/*.csv")],
                      ignore_index=True)

# save editorialTags in variable
et = big_frame['editorialTags']

# save allTags in variable
at = big_frame['allTags']

tags = getAllTags(et)
#tags = getAllTags(at)


# count uniq words and save words and counts in to lists
words = list(Counter(tags).keys())
counts = list(Counter(tags).values())

# create dict
dict_words = {'Label': words, 'Counts': counts}

# create and save dataframe to file
df = pd.DataFrame(dict_words)

df.to_csv('../zdf_data/cleaned/csv/ED_NODE.csv', encoding='utf-8-sig', sep=';')

print('done')