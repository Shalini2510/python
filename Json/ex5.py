#consuming rest api and get a dictionary from a json project

import requests
import json


r=requests.get("https://reqres.in/api/users?page=2")

if r.status_code == 200:
    d1= json.loads(r.text)
    print(d1)

else:
    print("could not get result from rest end point")