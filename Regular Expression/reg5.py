#  string - in jinja template variable are placed inside {{myname}} like this

import re
s1= "in jinja template variable are placed inside {{ myname }} like this"
val=re.search(r"\{\{(.*?)\}\}",s1)
if val:
    print(val.group(1))   #output-- myname
else:
    print("not found")