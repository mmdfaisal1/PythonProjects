# purse = dict()
#
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 5

# print(purse)

names = ['csev','cqen','csev','zqian','cqen']

count_dict = dict()

for name in names:
    count_dict[name] = count_dict.get(name, 0) + 1

print(count_dict)
