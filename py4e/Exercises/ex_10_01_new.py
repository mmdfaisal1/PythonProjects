fname = input('Please enter file name: ')

try:
    fhandle = open(fname)
except:
    print('File could not be opened', fname)
    quit()

email_dict = dict()

for line in fhandle:
    #line = line.rstrip()
    if line.startswith('From '):
        words_in_line = line.split()
        email = words_in_line[1]
        # for dict.get() function
        # https://www.py4e.com/html3/09-dictionaries
        email_dict[email] = email_dict.get(email, 0) + 1


list_of_emails = list()

for k, v in email_dict.items():
    newtup = (v, k)
    list_of_emails.append(newtup)

list_of_emails = sorted(list_of_emails, reverse=True)

# The following also works fine. It modifies the list (lists are mutable)
#list_of_emails.sort(reverse = True)


#To print the first item in the list
for k, v in list_of_emails[:1]:
    print(v, k)
