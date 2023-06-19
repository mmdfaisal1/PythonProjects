fname = input('Please enter file name: ')

try:
    fhandle = open(fname)
except:
    print('File could not be opened', fname)
    quit()

words_dict = dict()

for line in fhandle:
    words_in_line = line.split()
    for word in words_in_line:
        if word not in words_dict:
            words_dict[word] = 1

print(words_dict)

print(len(words_dict))
