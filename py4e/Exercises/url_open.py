import urllib.request
#from urllib import request

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#fhandle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
#fhandle = request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhandle:
    print(line.decode().strip())

#to retreive the headers
# https://docs.python.org/3/library/urllib.request.html
headers = fhandle.info()
print(headers)
