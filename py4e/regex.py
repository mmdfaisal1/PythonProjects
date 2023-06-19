import re

fhandle = open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    #if re.search('^From: ', line):
    #if re.search('^X.*:', line):
    if re.search('^X-\S+:', line):
        print(line)
