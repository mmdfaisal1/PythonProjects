import requests
import json
import xml.etree.ElementTree as ET

def gettoken():

    tree = ET.parse('sx_config.xml')
    token_url = tree.find('server/base_url').text + tree.find('token').text

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    username = tree.find('server/username').text
    password = tree.find('server/password').text
    payload = {'username': username, 'grant_type':'password', 'password': password}

    response = requests.get(token_url, headers=headers, data=payload, verify=False)

    js = json.loads(response.text)
    ret_token = 'bearer '+ js['access_token']
    return ret_token

def testfunction():
    token_var = gettoken()
    return token_var
