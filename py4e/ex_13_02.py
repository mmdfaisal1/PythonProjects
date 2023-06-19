import urllib.request, urllib.parse, urllib.error
import json

try:
    url = input('Enter the url: ')
except:
    print('The url is not valid')
    quit()

testurl1 = 'http://py4e-data.dr-chuck.net/comments_42.json'
testurl2 = 'http://py4e-data.dr-chuck.net/comments_101407.json'

urlhandle = urllib.request.urlopen(url)
data = urlhandle.read()

#print(data)
js = json.loads(data)

print(js['note'])

sum_count = 0

#Printing every value of count
for item in js['comments']:
    print(item['count'])

print('==================================')

#Calculating the count
for item in js['comments']:
    sum_count = sum_count + item['count']

print('The sum is ', sum_count)
