fname = input ("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print("File could not be opened")
    quit()

hour_dict = dict()

for line in fhandle:
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5]
    time_list = time.split(":")
    hour = time_list[0]
    hour_dict[hour] = hour_dict.get(hour, 0) + 1

#print(hour_dict)

mylist = list()
for key, value in hour_dict.items():
    tup = (key,value)
    mylist.append(tup)

#print(mylist)
mylist = sorted(mylist)
#print(mylist)

for k, v in mylist:
    print(k,v)
