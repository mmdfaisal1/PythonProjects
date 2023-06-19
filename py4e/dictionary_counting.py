line = input("Enter a line of text: ")

count_dict = dict()

words = line.split()
# print(words)

for word in words:
    count_dict[word] = count_dict.get(word, 0) + 1

# print(count_dict)

# for mykey in count_dict:
#     print(mykey, count_dict[mykey])

for aaa, bbb in count_dict.items():
    print(aaa,bbb)
