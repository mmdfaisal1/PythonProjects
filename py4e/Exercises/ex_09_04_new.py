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

#for key in email_dict:
#    print(key, email_dict[key])

bigemail = None
bigcount = None

# items() method returns a list of tuples
# https://www.py4e.com/html3/10-tuples
# >>> d = {'a':10, 'b':1, 'c':22}
# >>> t = list(d.items())
# >>> print(t)
# [('b', 1), ('a', 10), ('c', 22)]

for email, count in email_dict.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count

print(bigemail, bigcount)
