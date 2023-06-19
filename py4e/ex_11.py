import re
fname = input ("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print("File could not be opened")
    quit()

num_list = list()

for line in fhandle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) == 0:
        continue
    for num in numbers:
        num_list.append(float(num))

sum_num = sum(num_list)
print(sum_num)
