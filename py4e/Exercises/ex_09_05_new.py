fname = input('Please enter file name: ')

try:
    fhandle = open(fname)
except:
    print('File could not be opened', fname)
    quit()

domain_dict = dict()

for line in fhandle:
    #line = line.rstrip()
    if line.startswith('From '):
        words_in_line = line.split()
        email = words_in_line[1]
        email_parts = email.split('@')
        domain = email_parts[1]
        # for dict.get() function
        # https://www.py4e.com/html3/09-dictionaries
        domain_dict[domain] = domain_dict.get(domain, 0) + 1



for key,value in domain_dict.items():
    print(key,value)
