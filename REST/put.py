# PUT --- The POST method is used to create new resources, for updating a record
import requests
import json

r=requests.put("https://reqres.in/api/users/2",json={
    "name": "morpheus",
    "job": "zion resident"
})

if r.status_code == 200:
    d1=json.loads(r.text)
    print(d1)
else:
     print("unable to access",r.status_code)