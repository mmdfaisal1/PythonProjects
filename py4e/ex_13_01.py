import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

try:
    url = input('Enter the url: ')
except:
    print('The url is not valid')
    quit()

testurl1 = 'http://py4e-data.dr-chuck.net/comments_42.xml'
testurl2 = 'http://py4e-data.dr-chuck.net/comments_101406.xml'

urlhandle = urllib.request.urlopen(url)
data = urlhandle.read()
tree = ET.fromstring(data)

count_tag_list = tree.findall('.//count')

sum = 0
for item in count_tag_list:
    sum = sum + int(item.text)

print('The sum is ', sum)
