fname = input ("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print("File could not be opened")
    quit()

mylist = list()
for line in fhandle:
    line = line.rstrip()
    wordslist = line.split()
    for word in wordslist:
        if word not in mylist:
            mylist.append(word)

# print (mylist)

mylist.sort()
print(mylist)

# print(mylist.sort())
