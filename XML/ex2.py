import xml.etree.ElementTree as ET

tree=ET.parse('XML/movies.xml')

root=tree.getroot()

'''
print root.tag

print root.attrib
'''

for child in root.iter('movie'):
    print(child.tag, child.attrib)