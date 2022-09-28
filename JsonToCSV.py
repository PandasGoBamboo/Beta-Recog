import json
import csv
import pandas as pd
import os, glob

def list2String(list):
    split = []
    for item in list:
        if item == None:
            split.append("None")
        else:
            splitted = ", ".join(word for word in item)
            split.append(splitted)
    return split

in_dir = '../zdf_data/cleaned/'

out_dir = '../zdf_data/cleaned/csv/'

filename = '03_09_zdf_dokumentation_planet-e'

with open(in_dir + filename + '.json', 'r' , encoding='utf-8') as infile:
    
    data = pd.read_json(infile, orient='records', encoding='utf-8')

    src = pd.json_normalize(data['_source'])

    id = data['_id']
    src['id'] = id
   
    split_editorialTags = list2String(src['editorialTags'])
    split_allTags = list2String(src['allTags'])
    split_paths = list2String(src['additionalPaths'])

    src['editorialTags'] = split_editorialTags
    src['allTags'] = split_allTags
    src['additionalPaths'] = split_paths

    src.to_csv(out_dir + 'TESTESTESTEST' + filename + '.csv', encoding = 'utf-8-sig', index=False, sep=";")

    print('done')