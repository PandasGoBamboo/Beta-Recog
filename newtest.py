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