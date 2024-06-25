#json is inbuilt so we can directly import

import json 

d1={'name':'bob', 'age':10, 'class':'first'}

#closing file without calling close function

with(open("json/d1.json",'w')) as fh:   #fh--file handler
    json.dump(d1,fh)


    ######   OR    ###

#fh=open("d1.json",'w')  # to open a file

#json.dump(d1,fh)   #python object, file object

#fh.close()   #to close a file 