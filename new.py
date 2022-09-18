import xml.etree.ElementTree as ET

#uploaded = files.upload()

tree = ET.parse('test.xml')
root = tree.getroot()

# returns QUEID 'Metadaten' - 'Quelle' - 'QueID'
# print(root[1][10][0])

# print(root[2].tag)

# print(root.findall('PRAESENTATIONSFORM'))

# printet alle Tags in XML Datei, auch mehrfach aufkommende
# print([elem.tag for elem in root.iter()])

# sucht und printet Präsentationsform
for pform in root.iter('PRAESENTATIONSFORM'):
    print(pform.text)

# sucht und printent Text unter allen TITEL.Tags, also Hauptitel, Sonstiger Titel, Seitentitel
for titel in root.findall("./INHALT/TITEL/"):
    print(titel.text)

# sucht und printent Text unter VOLLTEXT.Tags
for text in root.findall("./INHALT/VOLLTEXT/"):
    print(text.text)


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
