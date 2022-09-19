import xml.etree.ElementTree as ET
import pandas as pd
import os


#directory = 'files'
directory = '2021'

# Erzeugt Listen, die später gefüllt werden
pforms = []
haupt_titels = []
sonst_titels = []
seiten_titels = []
texts = []

# Sucht alle Files in allen Subfoldern und speichert Daten in Listen
for root, subdirectories, files in os.walk(directory):
    for filename in files:
        file = os.path.join(root, filename)
        tree = ET.parse(file)
        root = tree.getroot()
        print(root[2].tag)
        for pform in root.iter('PRAESENTATIONSFORM'):
            pforms.append(pform.text)
        for haupt_titel in root.findall("./INHALT/TITEL/HAUPTTITEL"):
            haupt_titels.append(haupt_titel.text)
        for sonst_titel in root.findall("./INHALT/TITEL/SONSTIGER_TITEL"):
            sonst_titels.append(sonst_titel.text)
        for seiten_titel in root.findall("./INHALT/TITEL/SEITENTITEL"):
            seiten_titels.append(seiten_titel.text)
        for text in root.findall("./INHALT/VOLLTEXT/TEXT"):
            texts.append(text.text)

# Speichert Listen in Dataframe
train_data = pd.DataFrame(
    {'pform': pforms,
     'haupt_titel': haupt_titels,
     'sonst_titel': sonst_titels,
     'seiten_titel': seiten_titels,
     'volltext': texts,
    })


print(train_data.info)
