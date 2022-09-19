import os
import xml.etree.ElementTree as ET

directory = './files/'



# print(root[2].tag)

# sucht und findet files in allen ordnern unter angegebenen
for filename in os.listdir(directory):
    tree = ET.parse(filename)
    root = tree.getroot()
    print(root[2].tag)
    #print(os.path.join(root, filename))