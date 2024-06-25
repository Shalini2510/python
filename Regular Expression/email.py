#abc@gmail.com-(\b[a-z]+@[a-z]+\.[a-z]+)

import re
s1="the name of the employee is Bob Smith and his email is bobsmith@gmail.com and we have on more employee named Pat Smith and his email is patsmith@gmail.com"

p=re.compile(r'(\b[a-z]+@[a-z]+\.[a-z]+)')   #returns a regex object 

for val in p.finditer(s1):
    print(val.group(1))

#output : bobsmith@gmail.com
#         patsmith@gmail.com