from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
html = urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

for i in range(4):
    linknamelist = list()
    linktextlist = list()
    tags = soup('a')
    for tag in tags:
        linknamelist.append(tag.get('href', None))
        linktextlist.append(tag.contents[0])
    print(linknamelist[2])
    print(linktextlist[2])
    html = urlopen(linknamelist[2], context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

# for i in range(4):
#     print(i)
