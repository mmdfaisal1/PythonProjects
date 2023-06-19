fname = input('Please enter file name: ')

try:
    fhandle = open(fname)
except:
    print('File could not be opened', fname)
    quit()

email_list = list()
count = 0

for line in fhandle:
    #line = line.rstrip()
    if line.startswith('From '):
        count = count + 1
        words_in_line = line.split()
        email_list.append(words_in_line[1])

#print('The list of email addresses is', email_list)

for i in range(len(email_list)):
    print(email_list[i])

print(count)
