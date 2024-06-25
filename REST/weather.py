# openweathermap.org
# account - api key
# rest end point to collection weather information of given city - https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,APIKEY)
fh = open('REST/api_key','r')
APIKEY=fh.readline().strip() # replace API_KEY with your own api key
fh.close()
import requests
import json
#city_name=input("Enter your cityname")
#APIKEY=''
cities = ['Chennai','Mumbai','Bangalore','Delhi']
def getTemperature(city_name):
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,APIKEY))
    #r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=0d82c47a56a20ee1ea11d9d6fa1b2ff2)
    if r.status_code==200:
        d1 = json.loads(r.text) # r.text - text value returned from rest end point
        #print(d1)
        city_temp = d1.get('main').get('temp')-273.15
        print("The temperature at %s is %.2f celsius" %(city_name,city_temp))
    else:
        print("problem in getting weather information")
for city in cities:
    getTemperature(city)