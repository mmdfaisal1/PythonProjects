import requests
import json

url = 'https://mf2012-06.npb.local:9777/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = {'username':'npb\mfuser1', 'grant_type':'password', 'password':'Admin1234'}

response = requests.get(url, headers=headers, data=payload, verify=False)

# print(response.status_code)
# print(response.headers)
# print(response.text)

js = json.loads(response.text)
mytoken = 'bearer '+ js['access_token']

url1 = 'https://mf2012-06.npb.local:9777/api/v2/scan/policy'
headers1 = {'Content-Type': 'application/json',
            'Authorization': mytoken}
payload1 = {
            'Path': [
            '\\\\mf2012x64.npb.local\\test1'
            ],
            'Name': 'scan1',
            'Description': 'test desc',
            'ScanOptions': {
                            'DataEngineChoice': 'eUseSystemSelectedAgent'
                            }
            }

#The following works fine too. (http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request)
#response1 = requests.post(url1, headers=headers1, data=json.dumps(payload1), verify=False)

response1 = requests.post(url1, headers=headers1, json=payload1, verify=False)

js1 = json.loads(response1.text)

if response1.status_code==201 and js1['Name']=='scan1':
    print('The test passed.', js1['Name'], 'created with path ', js1['Path'])
else:
    print('The test failed')
