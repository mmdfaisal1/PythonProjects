fname = input ("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print("File could not be opened")
    quit()

count = 0

for line in fhandle:
    if not line.startswith('From '):
        continue
    mylist = line.split()
    print(mylist[1])
    count = count + 1

print('There are', count, 'email addresses')
