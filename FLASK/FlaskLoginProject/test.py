import requests
import json

username="bob"
password="bob@123"
headers={"Content-Type":"application/json"}
data = {"username":username, "password":password}
#r=requests.post("http://127.0.0.1:5000/api/register",headers=headers,data=json.dumps(data))

#to run password protected url
r=requests.get("http://127.0.0.1:5000/api/dothis", auth=("bob","bob123"))

#if we not give username and password it will show unauthorized access
#r=requests.get("http://127.0.0.1:5000/api/dothis")
print(r.status_code)
print(r.text)