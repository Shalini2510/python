#convert str into dict

import json

s2= '{"name":"pat", "age":12, "class":"third"}'

print(type(s2))

d2= json.loads(s2)

print(type(d2))

print(d2)