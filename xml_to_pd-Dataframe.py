from multiprocessing.sharedctypes import Value
import xml.etree.ElementTree as ET
import pandas as pd
import os
from collections import Counter
from lxml import etree
from datetime import datetime

# Counter für Dauer von Skriptausführung
startTime = datetime.now()

# Konsolenoutput
print('ich roedel in ' + directory + ' ....')

# Dateipfad
directory = 'C:/Users/tschu/Desktop/Daten neu/xx'

# Erstelle Listen zum Befüllen
pforms = []
haupt_titels = []
texts = []
# weiteres Feature = []

# relevante Präsentationsformen
pform_vars = ['KOM', 'INT', 'GRF', 'REP', 'REZ', 'ESS', 'CHR'] # weitere Pformen hinzufügen

# iteriert durch alle Ordner und Subordner in angegebenen Dateipfad
for roots, subdirectories, files in os.walk(directory):
    for filename in files:
        try:
            # initiert Parser für xml.Dateien
            parser1 = ET.XMLParser(encoding='utf-8')
            file = os.path.join(roots, filename)
            tree = ET.parse(file, parser=parser1)
            root = tree.getroot()

            # checkt, ob alle relevanten xml-Elemente vorhanden sind, wenn eins fehlt, wird Datei geskippt
            pformfind = root.findall('.//PRAESENTATIONSFORM')
            titelfind = root.findall('.//HAUPTTITEL')
            textfind = root.findall('.//TEXT')
            # Hier weitere zu testende Features hinzufügen  
        
            if not pformfind or not titelfind or not textfind: # or not weitere Feature
                continue

            # fügt den leeren Listen jeweils eine Pform, einen Titel und den Text hinzu, abhängig davon, 
            # ob eine Pform vorhanden ist. Ist der Titel oder der Text leer, wird ein Platzhalter hinzugefügt.
            else:
                for pform in root.iter('PRAESENTATIONSFORM'):
                    if (pform.text in pform_vars):
                        pforms.append(pform.text)
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
                        # weitere for-Loops bei weiteren Featuren
        except ET.ParseError:
            print('{} is corrupt'.format(file))

# Speichere Listen in Dataframe
train_data = pd.DataFrame(
        {'pform': pforms,
        'haupt_titel': haupt_titels,
        'volltext': texts,
        # 'feature': feature_liste
})

# printet Kopf und Info von Dataframe
print(train_data.info)

# speichert Dataframe in Pickle-Datei 
train_data.to_pickle('raw_data.pkl')

# Konsolenoutput
print('ich habe fertig')
print(datetime.now() - startTime)
