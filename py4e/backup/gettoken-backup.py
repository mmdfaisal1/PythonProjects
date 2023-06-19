import requests
import json


url = 'https://mf2012-06.npb.local:9777/token'

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

payload = {'username':'npb\mfuser1', 'grant_type':'password', 'password':'Admin1234'}

response = requests.get(url, headers=headers, data=payload, verify=False)

# print(response.status_code)
# print(response.headers)
# print(response.text)
# print('________________________________________________________')

js = json.loads(response.text)
print(js['access_token'])
