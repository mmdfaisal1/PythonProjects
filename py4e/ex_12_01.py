from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
html = urlopen('http://py4e-data.dr-chuck.net/comments_101404.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

numbers_list = list()

tags = soup('span')
for tag in tags:
    number = int(tag.contents[0])
    numbers_list.append(number)

print('The Sum of number is: ', sum(numbers_list))
