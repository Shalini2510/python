#get the python object from json file


import json

with(open("Json/d1.json",'r')) as fh:
    d2=json.load(fh)
    print(d2)

