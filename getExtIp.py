import requests
print(requests.get('https://api.ipify.org?format=json').json()['ip'])