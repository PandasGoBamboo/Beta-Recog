import xml.etree.ElementTree as ET
import pandas as pd
import os
from collections import Counter
from lxml import etree

# Datenablageort
directory = 'C:/Users/tschu/Desktop/Daten neu/xx/2016'


pforms = []
haupt_titels = []
sonst_titels = []
seiten_titels = []
texts = []

print('ich roedel......')

# Sucht alle Files in allen Subfoldern und speichert sie in Liste
for roots, subdirectories, files in os.walk(directory):
    for filename in files:
        # fängt korrupte xml-Files ab und ignoriert sie
        try:
            parser1 = ET.XMLParser(encoding='utf-8')
            file = os.path.join(roots, filename)
            tree = ET.parse(file, parser=parser1)
            root = tree.getroot()
            for pform in root.iter('PRAESENTATIONSFORM'):
                pforms.append(pform.text)
            for haupt_titel in root.findall("./INHALT/TITEL/HAUPTTITEL"):
                haupt_titels.append(haupt_titel.text)
            for text in root.findall("./INHALT/VOLLTEXT/TEXT"):
                texts.append(text.text)
        except ET.ParseError:
            print('{} is corrupt'.format(file))

# erstellt Dataframe aus Liste
"""
train_data = pd.DataFrame(
    {'pform': pforms,
     'haupt_titel': haupt_titels,
     'volltext': texts,
    })

"""

# Zählt unique Keys und speichert sie mit Bezeichnung in Liste
"""
keys = Counter(pforms).keys() # equals to list(set(words))
values = Counter(pforms).values() # counts the elements' frequency

liste = pd.DataFrame(
    {
        'Pform': keys,
        'Anzahl': values
    }
)

print(liste)
# Liste als CSV
#liste.to_csv('2018.csv') 

"""

print('ich habe fertig')