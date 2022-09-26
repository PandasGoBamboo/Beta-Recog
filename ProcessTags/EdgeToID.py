import json, csv, pandas as pd 
from collections import Counter
import itertools

# lädt nodes und edges Datei
nodes = pd.read_csv('../zdf_data/cleaned/csv/analysis/test_nodes.csv', sep=';', encoding='utf-8', dtype='unicode')
edges = pd.read_csv('../zdf_data/cleaned/csv/analysis/edges_Edi_wNames_FULL.csv', sep=';', encoding='utf-8', dtype='unicode')

# speichert Spalten in einzelne Variablen
src = edges['source']
target = edges['target']
weight = edges['weight']

# erzeugt neue Listen für spätere Speicherung
new_src = []
new_target = []

# erzeugt Dictionary mit Id: Label Zuweisung
res = dict(zip(nodes.Id, nodes.Label))
# dreht Ids und Labels
new_nodes = dict((v,k) for k,v in res.items())

# Schleife die Wörter durch Ids in Source-Spalte ersetzt
for tag in src: 
    for k, v in new_nodes.items():
        if k == tag:
            tag = v
    new_src.append(tag)

# Schleife die Wörter durch Ids in Target-Spalte ersetzt
for tag in target:
    for k, v in new_nodes.items():
        if k == tag:
            tag = v
    new_target.append(tag)

# Erzeugt Liste aus drei Spalten
data = zip(new_src, new_target, weight)

# Erzeugt DataFrame aus den drei Spalten
new_df = pd.DataFrame(data, columns = ['source', 'target', 'weight'])

# Speichern in Datei
new_df.to_csv('../zdf_data/cleaned/csv/analysis/TESTTEST.csv', encoding='utf-8-sig', sep=';')
print('FINITO')

