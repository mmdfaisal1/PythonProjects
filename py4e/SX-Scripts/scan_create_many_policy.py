import requests
import json
import time
import xml.etree.ElementTree as ET
from functions_file import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

tree_sx_config = ET.parse('sx_config.xml')

url = tree_sx_config.find('server/base_url').text + tree_sx_config.find('api/scan/create').text

scanapiheaders = getapiheaders()

with open("scan_names.txt", "r") as fh:
    scan_names_list = fh.read().splitlines()

with open("path_names.txt", "r") as fh:
    path_names_list = fh.read().splitlines()

for i in range(len(scan_names_list)):
    payload = {
                'Path': [path_names_list[(i*3)],path_names_list[(i*3)+1],path_names_list[(i*3)+2]],
                'Name': scan_names_list[i],
                'Description': 'test desc',
                'ScanOptions': {'DataEngineChoice': 'eUseSystemSelectedAgent'}
              }

    response = requests.post(url, headers=scanapiheaders, json=payload, verify=False)
    time.sleep(5)

# js = json.loads(response.text)
#
# print("--------------------------------------------------------------------------------")
# if response.status_code==201 and js['Name']=='scan1':
#     print('The test passed.', js['Name'], 'created with path ', js['Path'])
# else:
#     print('The test failed')
