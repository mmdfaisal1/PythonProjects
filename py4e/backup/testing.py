import requests
import json
import xml.etree.ElementTree as ET
from functions_file import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

mytoken = testfunction()
print(mytoken)
