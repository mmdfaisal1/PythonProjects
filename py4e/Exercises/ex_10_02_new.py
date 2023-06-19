fname = input('Please enter file name: ')

try:
    fhandle = open(fname)
except:
    print('File could not be opened', fname)
    quit()

hours_dict = dict()

for line in fhandle:
    #line = line.rstrip()
    if line.startswith('From '):
        words_in_line = line.split()
        time = words_in_line[5]
        time_parts = time.split(':')
        hour = time_parts[0]
        # for dict.get() function
        # https://www.py4e.com/html3/09-dictionaries
        hours_dict[hour] = hours_dict.get(hour, 0) + 1



for key,value in hours_dict.items():
    print(key,value)
