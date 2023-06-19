import xml.etree.ElementTree as ET
import urllib.request

testurl1 = 'http://py4e-data.dr-chuck.net/comments_42.xml'
testurl2 = 'http://py4e-data.dr-chuck.net/comments_101406.xml'


try:
    url = input('Enter url: ')
    url_handle = urllib.request.urlopen(url)
except:
    print('Not a valid url')
    quit()

#THE PARSE FUNCTION CAN TAKE IN INPUT EITHER FILE NAME OR FILE OBJECT CONTAINING XML DATA
# xml.etree.ElementTree.parse(source, parser=None)
# Parses an XML section into an element tree. source is a filename or file object containing XML data
# https://docs.python.org/3/library/xml.etree.elementtree.html


tree = ET.parse(url_handle)

tag_list_counts = tree.findall('comments/comment/count')
# or the following
# tag_list_counts = tree.findall('.//count')


sum = 0

for item in tag_list_counts:
    sum = sum + int(item.text)

print('The sum of the numbers is', sum)
