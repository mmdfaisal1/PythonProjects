fhandle = open('mbox.txt')
count = 0
for x in fhandle:
    count = count + 1
print('Total Lines in the File: ', count )
