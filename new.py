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
# sucht und printet Präsentationsform
for pform in root.iter('PRAESENTATIONSFORM'):
    #print(pform.text)
    pforms.append(pform.text)
    #df['pform'] = pform.text

titels = []
# sucht und printent Text unter allen TITEL.Tags, also Hauptitel, Sonstiger Titel, Seitentitel
for titel in root.findall("./INHALT/TITEL/"):
    #print(titel.text)
    titels.append(titel.text)
    #df['titel'] = titel.text

texts = []
# sucht und printent Text unter VOLLTEXT.Tags
for text in root.findall("./INHALT/VOLLTEXT/"):
    #print(text.text)
    texts.append(text.text)
    #df['text'] = text.text

print(pforms)
print(titels)
print(texts)

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
