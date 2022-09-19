import os
import xml.etree.ElementTree as ET

directory = 'files'


# sucht alle files in allen subfoldern, öffnet xml und printet
for root, subdirectories, files in os.walk(directory):
    for filename in files:
        file = os.path.join(root, filename)
        tree = ET.parse(file)
        root = tree.getroot()
        print(root[2].tag)
