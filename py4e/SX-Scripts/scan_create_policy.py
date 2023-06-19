import requests
import json
import xml.etree.ElementTree as ET
from functions_file import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

tree_sx_config = ET.parse('sx_config.xml')

url = tree_sx_config.find('server/base_url').text + tree_sx_config.find('api/scan/create').text

scanapiheaders = getapiheaders()

payload = {
            'Path': [
            '\\\\mf2012x64.npb.local\\test1'
            ],
            'Name': 'scan1',
            'Description': 'test desc',
            'ScanOptions': {
                            'DataEngineChoice': 'eUseSystemSelectedAgent'
                            }
          }

# The following works fine too. (http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request)
# response1 = requests.post(url1, headers=headers1, data=json.dumps(payload1), verify=False)

response = requests.post(url, headers=scanapiheaders, json=payload, verify=False)

js = json.loads(response.text)

print("--------------------------------------------------------------------------------")
if response.status_code==201 and js['Name']=='scan1':
    print('The test passed.', js['Name'], 'created with path ', js['Path'])
else:
    print('The test failed')
