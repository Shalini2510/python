#POST ---> The POST method is used to create new resources.
#https://reqres.in/ use this website for GET, POST 

import requests
import json

r=requests.post("https://reqres.in/api/users",json={
    "name": "morpheus",
    "job": "leader"
})

if r.status_code == 201:
    d1=json.loads(r.text)
    print(d1)
else:
    print("unable to access",r.status_code)