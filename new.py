import xml.etree.ElementTree as ET

#uploaded = files.upload()

tree = ET.parse('test.xml')
root = tree.getroot()

# returns QUEID 'Metadaten' - 'Quelle' - 'QueID'
#print(root[1][10][0])

for elem in root[2]:
  #if elem.text != None:
    print(elem.text)
    for subelem in elem:
      if subelem.text != None:
        print(subelem.text)
