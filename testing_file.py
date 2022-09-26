import xml.etree.ElementTree as ET
import pandas as pd
import os
from collections import Counter
from lxml import etree

directory = 'files'
directory = 'C:/Users/tschu/Desktop/Daten neu/xx/2016'


pforms = []
haupt_titels = []
sonst_titels = []
seiten_titels = []
texts = []

print('ich roedel......')
# sucht alle files in allen subfoldern und speichert sie in Dataframe
for roots, subdirectories, files in os.walk(directory):
    for filename in files:
        try:
            parser1 = ET.XMLParser(encoding='utf-8')
            file = os.path.join(roots, filename)
            tree = ET.parse(file, parser=parser1)
            root = tree.getroot()
            #print(root[2].tag)
            for pform in root.iter('PRAESENTATIONSFORM'):
                pforms.append(pform.text)
        except ET.ParseError:
            print('{} is corrupt'.format(file))

        """
        for haupt_titel in root.findall("./INHALT/TITEL/HAUPTTITEL"):
            haupt_titels.append(haupt_titel.text)
        for sonst_titel in root.findall("./INHALT/TITEL/SONSTIGER_TITEL"):
            sonst_titels.append(sonst_titel.text)
        for seiten_titel in root.findall("./INHALT/TITEL/SEITENTITEL"):
            seiten_titels.append(seiten_titel.text)
        for text in root.findall("./INHALT/VOLLTEXT/TEXT"):
            texts.append(text.text)
        """


"""
train_data = pd.DataFrame(
    {'pform': pforms,
     'haupt_titel': haupt_titels,
     'sonst_titel': sonst_titels,
     'seiten_titel': seiten_titels,
     'volltext': texts,
    })

"""

# Zählt unique Keys und speichert sie mit Bezeichnung in Liste
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

print('ich habe fertig')

"""
print(len(haupt_titels)) # 1749
print(len(sonst_titels)) # 1426
print(len(seiten_titels)) # 1253
print(len(texts)) # 1749
print(len(pforms)) # 1875

"""


"""
print(train_data.head)
print(pforms)
print(haupt_titels)
print(sonst_titels)
print(seiten_titels)
print(texts)

"""

"""
# root[2] = Inhalt
for elem in root[2]:
  #if elem.text != None:
    print(elem.tag)
    for subelem in elem:
      if subelem.text != None:
        print('----')
        print(subelem.text)

"""
