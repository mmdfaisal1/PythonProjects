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
        #>>> counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
        #>>> print(counts.get('jan', 0))
        #100
        #>>> print(counts.get('tim', 0))
        #0
        email_dict[email] = email_dict.get(email, 0) + 1

print(email_dict)

print('\n\n')

for key in email_dict:
    print(key, email_dict[key])
