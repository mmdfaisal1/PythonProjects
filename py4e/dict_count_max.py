fname = input ("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print("File could not be opened")
    quit()

count_dict = dict()

for line in fhandle:
    words = line.split()
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1

#print(count_dict)

for aaa, bbb in count_dict.items():
    print(aaa,bbb)

bigcount = None
bigword = None
for word, count in count_dict.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
