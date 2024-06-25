#find multiple matches

import re
s1="the name of the employee is Bob Smith and his designation is developer and we have on more employee named Pat Smith and his designation is devops"

p=re.compile(r'(\b[A-Z][a-z]+\s[A-Z][a-z]+\b)')   #returns a regex object 

for val in p.finditer(s1):
    print(val.group(1))

#output - Bob Smith 
#         Pat Smith