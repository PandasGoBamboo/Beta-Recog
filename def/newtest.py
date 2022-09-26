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
        count = 0
        for word in split:
            count += 1
        all.append(count)

    return all

path = ('../zdf_data/cleaned/csv')

# create one big df from every document in path
big_frame = pd.concat([pd.read_csv(f, sep=';') for f in glob.glob(path + "/*.csv")],
                      ignore_index=True)

# save editorialTags in variable
et = big_frame['editorialTags']

# save allTags in variable
at = big_frame['allTags']

tags = getAllTags(et)
tags2 = getAllTags(at)

ziped = zip(tags, tags2)

# create and save dataframe to file
df = pd.DataFrame(ziped, columns=['Count Editorials', 'Count AllTags'])

print(df.var())
print()

df.to_csv('../zdf_data/cleaned/csv/analysis/countsoftags.csv', encoding='utf-8-sig', sep=';')

print('done')

