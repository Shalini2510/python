import xml.etree.ElementTree as ET

tree=ET.parse('XML/movies.xml')

root=tree.getroot()

'''
print root.tag

print root.attrib
'''

for m in root.findall("./genre/decade/movie/[year='1992']"):
    print(m.attrib)