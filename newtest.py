from cgitb import text
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

pform_vars = ['KOM', 'INT', 'GRF', 'REP', 'REZ', 'ESS', 'CHR']

for roots, subdirectories, files in os.walk(directory):
    for filename in files:
        # fängt korrupte xml-Files ab und ignoriert sie
        try:
            parser1 = ET.XMLParser(encoding='utf-8')
            file = os.path.join(roots, filename)
            tree = ET.parse(file, parser=parser1)
            root = tree.getroot()
           
            pformfind = root.findall('.//PRAESENTATIONSFORM')
            titelfind = root.findall('.//HAUPTTITEL')
            textfind = root.findall('.//TEXT')

            if not pformfind or not titelfind or not textfind:
                continue
            else:
                for pform in root.iter('PRAESENTATIONSFORM'):
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
                    pforms.append(pform.text)
        except ET.ParseError:
            print('{} is corrupt'.format(file))


train_data = pd.DataFrame(
        {'pform': pforms,
        'haupt_titel': haupt_titels,
        'volltext': texts,
    })


print(len(pforms))
print(len(haupt_titels))
print(len(texts))



print(train_data.head)


print('ich habe fertig')

