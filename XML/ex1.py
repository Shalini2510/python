import xml.etree.ElementTree as ET

tree=ET.parse('XML/movies.xml')

root=tree.getroot()

'''
print root.tag

print root.attrib
'''

#print the child of the root
#for child in root.iter():
    #print(child.tag, child.attrib)

#for child in root.iter('movie):
    #print(child.tag, child.attrib)

for child in root.iter():
    print(child.tag, child.attrib)