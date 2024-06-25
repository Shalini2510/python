#GET --->  The GET method is used to retrieve data on a server. 

import requests
import json

r=requests.get("https://reqres.in/api/users?page=2")

if r.status_code == 200:
    d1=json.loads(r.text)
    print(d1)
else:
    print("unable to access",r.status_code)