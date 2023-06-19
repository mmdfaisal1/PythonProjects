fname = input('Please enter file name: ')

try:
    fhandle = open(fname)
except:
    print('File could not be opened', fname)
    quit()

days_dict = dict()

for line in fhandle:
    #line = line.rstrip()
    if line.startswith('From '):
        words_in_line = line.split()
        day = words_in_line[2]
        # for dict.get() function
        # https://www.py4e.com/html3/09-dictionaries
        days_dict[day] = days_dict.get(day, 0) + 1

print(days_dict)
