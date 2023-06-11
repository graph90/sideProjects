import requests
import json
import sys

def getLocationBasedOnIp():
    url = "http://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()
    location = data['loc'].split(',')
    return (location[0], location[1])
lat, lon = getLocationBasedOnIp()
print(lat, lon)