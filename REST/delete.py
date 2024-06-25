#DELETE --> The DELETE method is used to remove data from a database

import requests
import json

r=requests.delete("https://reqres.in/api/users/2")

if r.status_code == 204:
    d1=json.loads(r.text)
    print(d1)
else:
     print("unable to access",r.status_code)