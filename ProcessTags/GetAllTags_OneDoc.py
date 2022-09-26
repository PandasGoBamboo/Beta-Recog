import json
import pandas as pd 
import csv

def writeTags(tags):
    split = []
    for item in tags:
        if item != None:
            split.append(str(item))
        else:
            continue
    return split

in_dir = '../zdf_data/cleaned/csv/'
out_dir = '../zdf_data/cleaned/csv/test/'
filename = '03_09_zdf_dokumentation_37-grad'

file = pd.read_csv(in_dir + filename + '.csv', encoding='utf-8', delimiter=';')

splitted_editorials = writeTags(file['editorialTags'])

print(splitted_editorials)

splitted_all = writeTags(file['allTags'])


df = pd.DataFrame(data= {'Editorials': [splitted_editorials], 'AllTags': [splitted_all], 'EveryTag': [splitted_editorials + splitted_all],
 'docCount': None, 'textLength': None, 'textLenMax': None, 'textLenMin': None, 'textLenMean': None, 'AllPaths': None, 'viewCountTotal': None,
  'viewCountMin': None, 'viewCountMax': None, 'viewCountMean': None}, index=[filename])

df.to_csv(out_dir + 'analyze.csv', encoding = 'utf-8-sig', sep=";", mode = 'a')

# MAN KANN NICHT ALLE TAGS IN EINER ZEILE SPEICHERN

