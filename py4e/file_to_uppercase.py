fname = input ("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print("File could not be opened")
    quit()

file_read = fhandle.read()
file_read_upper = file_read.upper()
print(file_read_upper)
