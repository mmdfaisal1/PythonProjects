fname = input('Please enter file name: ')

try:
    fhandle = open(fname)
except:
    print('File could not be opened', fname)
    quit()

words_list = list()

#Going through each line in the file
#'line' is a string
#'words_in_line' is a list
for line in fhandle:
    words_in_line = line.split()
    #Going through each word(item) in the line(list)
    for word in words_in_line:
        if word not in words_list:
            words_list.append(word)

#The following does not work. Sort() is function which returns something
#print('The sorted list of words is', words_list.sort())

words_list.sort()
print('The sorted list of words is', words_list)
