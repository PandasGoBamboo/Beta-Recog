import xml.etree.ElementTree as ET
import pandas as pd
import os
from collections import Counter
from lxml import etree

# Datenablageort
directory = 'C:/Users/tschu/Desktop/BETA-RECOG/2021'


pforms = []
haupt_titels = []
texts = []

print('ich roedel......')


for roots, subdirectories, files in os.walk(directory):
    for filename in files:
        # fängt korrupte xml-Files ab und ignoriert sie
        try:
            parser1 = ET.XMLParser(encoding='utf-8')
            file = os.path.join(roots, filename)
            tree = ET.parse(file, parser=parser1)
            root = tree.getroot()
            try:
                for data in root.iter('ARTIKEL'):
                    pform = (data[1][15])
                    #haupt_titel = (data[2][0][0])
                    #text = (data[2][1][0])
                    if not pform: #or not haupt_titel or not text:
                        continue
                    else:
                        pforms.append(pform.text)
                        #haupt_titels.append(haupt_titel.text)
                        #texts.append(text.text)
       
            except IndexError:
                print('{} is out of Range'.format(file))
        except ET.ParseError:
            print('{} is corrupt'.format(file))

for roots, subdirectories, files in os.walk(directory):
    for filename in files:
        # fängt korrupte xml-Files ab und ignoriert sie
        try:
            parser1 = ET.XMLParser(encoding='utf-8')
            file = os.path.join(roots, filename)
            tree = ET.parse(file, parser=parser1)
            root = tree.getroot()
            pform = root.findall('PRAESENTATIONSFORM_LISTE')
            titel = root.findall('HAUPTTITEL')
            text = root.findall('VOLLTEXT')

            if not pform or not titel or not text:
                continue
            else:
                pforms.append(pform.text)
                haupt_titels.append(titel.text)
                texts.append(text.text)

        except ET.ParseError:
            print('{} is corrupt'.format(file))


print(len(pforms))
print(len(haupt_titels))
print(len(texts))


"""
train_data = pd.DataFrame(
    {'pform': pforms,
     'haupt_titel': haupt_titels,
     'volltext': texts,
    })

print(train_data.head)

"""

# Zählt unique Keys und speichert sie mit Bezeichnung in Liste

#keys = Counter(pforms).keys() # equals to list(set(words))
#values = Counter(pforms).values() # counts the elements' frequency
#keys2 = Counter(haupt_titels).keys()
#values2 = Counter(haupt_titels).values()
#keys3 = Counter(texts).keys()
#alues3 = Counter(texts).values()


"""
liste = pd.DataFrame(
    {
        'Titel Anzahl': values2
    }
)

print(liste)
# Liste als CSV
#liste.to_csv('2018.csv') 

"""

print('ich habe fertig')

"""
            # liefert nur das Element an angegebener Indexposition zurück
            for index, pform in enumerate(root.iter('PRAESENTATIONSFORM')):

                if not pform:
                    pforms.append('Platzhalter')
                elif index == 0:
                    pforms.append(pform.text)
            for index, haupt_titel in enumerate(root.iter('HAUPTTITEL')):
                if not haupt_titel:
                    haupt_titels.append('Platzhalter')
                elif index == 0:
                    haupt_titels.append(haupt_titel.text)
            for index, text in enumerate(root.iter('TEXT')):
                if not text:
                    texts.append('Platzhalter')
                elif index == 0:
                    texts.append(text.text)
"""

"""
for roots, subdirectories, files in os.walk(directory):
    for filename in files:
        # fängt korrupte xml-Files ab und ignoriert sie
        try:
            parser1 = ET.XMLParser(encoding='utf-8')
            file = os.path.join(roots, filename)
            tree = ET.parse(file, parser=parser1)
            root = tree.getroot()
            
            # liefert nur das Element an angegebener Indexposition zurück
            for index, pform in enumerate(root.iter('PRAESENTATIONSFORM')):
                if index == 0:
                    pforms.append(pform.text)
            
            for haupt_titel in root.findall("./INHALT/TITEL/HAUPTTITEL"):
                haupt_titels.append(haupt_titel.text)
            
            for text in root.findall("./INHALT/VOLLTEXT/TEXT"):
                texts.append(text.text)
        except ET.ParseError:
            print('{} is corrupt'.format(file))

"""