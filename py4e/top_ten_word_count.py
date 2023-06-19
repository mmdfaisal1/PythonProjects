fname = input ("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print("File could not be opened")
    quit()

word_count_dict = dict()

for line in fhandle:
    words = line.split()
    for word in words:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

mylist = list()
for key, val in word_count_dict.items():
    newtup = (val, key)
    mylist.append(newtup)

mylist = sorted(mylist, reverse = True)

for val, key in mylist[:10]:
    print(key, val)

    
