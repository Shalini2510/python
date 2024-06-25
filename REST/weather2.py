import threading
import requests
import json
import time

fh = open('REST/api_key','r')

APIKEY=fh.readline().strip()

fh.close()


def get_temperature(city_name,n):
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,APIKEY))
    time.sleep(2)
    if r.status_code==200:
        d1 = json.loads(r.text)
        #print(d1)
        city_temp = d1.get('main').get('temp')-273.15
        print("The temperature at %s is %.2f celsius" %(city_name,city_temp))
    else:
        print("problem in getting weather information")
    
    
cities=['bangalore','mumbai','chennai']

for i in range(len(cities)):
    t1 = threading.Thread(target=get_temperature,args=(cities[i],i+2))
    t1.start()