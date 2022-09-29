from cgitb import text
import xml.etree.ElementTree as ET
import pandas as pd
import os
from collections import Counter
from lxml import etree

# Datenablageort
directory = 'C:/Users/tschu/Desktop/BETA-RECOG/newtest'


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
            # for data in root.iter('ARTIKEL'):
            # liefert nur das Element an angegebener Indexposition zurück

            # !!!!vorher ein Check machen, ob Tags existent sind!!!!
            # testen was passiert wenn Tag fehlt mit

            # geh in jedes File. Schau, ob es ein Element pform gibt? 
            # hier findet er schon das nicht
            pformfind = root.findall('.//PRAESENTATIONSFORM')
            titelfind = root.findall('.//HAUPTTITEL')
            textfind = root.findall('.//TEXT')

            if not pformfind or not titelfind or not textfind:
                continue
            else:
                for pform in root.iter('PRAESENTATIONSFORM'):
                    pforms.append(pform.text)
                        # gibts das feld überhaupt, wenn nicht Platzhalter, wenn doch to das
                    for haupt_titel in root.iter('HAUPTTITEL'):
                        if haupt_titel.text is not None:
                                haupt_titels.append(haupt_titel.text)
                        else:
                            haupt_titels.append('xxxPlatzhalterxxx')
                    for text in root.iter('TEXT'):
                        if text.text is not None:
                            texts.append(text.text)
                        else:
                            texts.append('xxxPlatzhalterxxx') 
        except ET.ParseError:
            print('{} is corrupt'.format(file))

print(len(pforms))
print(len(haupt_titels))
print(len(texts))




train_data = pd.DataFrame(
        {'pform': pforms,
        'haupt_titel': haupt_titels,
        'volltext': texts,
    })

print('{} is sdfsdf'.format(file))

print(train_data.head)

#train_data.to_csv('testfile.csv', encoding = 'utf-8-sig', index=False, sep=";")


# Zählt unique Keys und speichert sie mit Bezeichnung in Liste

# keys = Counter(pforms).keys() # equals to list(set(words))
# values = Counter(pforms).values() # counts the elements' frequency
# keys2 = Counter(haupt_titels).keys()
# values2 = Counter(haupt_titels).values()
# keys3 = Counter(texts).keys()
# alues3 = Counter(texts).values()


"""
liste = pd.DataFrame(
    {
        'Titel Anzahl': values2
    }
)

print(liste)
# Liste als CSV
# liste.to_csv('2018.csv') 

"""

print('ich habe fertig')


"""
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
                    pform = (data[1][15][0].text)
                    print(data[1][15][0].text)
                    if not pform:
                        continue
                    else:
                        pforms.append(pform)
            except IndexError:
                print('{} is out of Range'.format(file))
        except ET.ParseError:
            print('{} is corrupt'.format(file))

"""
