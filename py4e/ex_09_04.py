fname = input ("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print("File could not be opened")
    quit()

email_dict = dict()

for line in fhandle:
    if not line.startswith('From '):
        continue
    words = line.split()
    email_address = words[1]
    email_dict[email_address] = email_dict.get(email_address, 0) + 1

print(email_dict)

bigcount = None
bigword = None
for email, count in email_dict.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count

print(bigword, bigcount)
