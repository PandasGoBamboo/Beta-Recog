import xml.etree.ElementTree as ET
import pandas as pd

#uploaded = files.upload()

tree = ET.parse('test.xml')
root = tree.getroot()

# returns QUEID 'Metadaten' - 'Quelle' - 'QueID'
# print(root[1][10][0])

# print(root[2].tag)

# print(root.findall('PRAESENTATIONSFORM'))

# printet alle Tags in XML Datei, auch mehrfach aufkommende
# print([elem.tag for elem in root.iter()])


pforms = []
# sucht Präsentationsform und fügt sie zur Liste hinzu
for pform in root.iter('PRAESENTATIONSFORM'):
    pforms.append(pform.text)

haupt_titels = []
# sucht Haupttitel und fügt sie ihn Liste hinzu
for haupt_titel in root.findall("./INHALT/TITEL/HAUPTTITEL"):
    haupt_titels.append(haupt_titel.text)

sonst_titels = []
# sucht sonstige Titel und fügt ihn zur Liste hinzu
for sonst_titel in root.findall("./INHALT/TITEL/SONSTIGER_TITEL"):
    sonst_titels.append(sonst_titel.text)

seiten_titels = []
# sucht Seitentitel und fügt ihn zur Liste hinzu
for seiten_titel in root.findall("./INHALT/TITEL/SEITENTITEL"):
    seiten_titels.append(seiten_titel.text)

texts = []
# such Volltext-Text und fügt ihn zur Liste hinzu
for text in root.findall("./INHALT/VOLLTEXT/TEXT"):
    texts.append(text.text)

train_data = pd.DataFrame(
    {'pform': pforms,
     'haupt_titel': haupt_titels,
     'sonst_titel': sonst_titels,
     'seiten_titel': seiten_titels,
     'volltext': texts,
    })
print(train_data.head)

#print(pforms)
#print(haupt_titels)
#print(sonst_titels)
#print(seiten_titels)
#print(texts)

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
