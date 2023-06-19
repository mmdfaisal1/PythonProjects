mydict = {'a':10, 'b':1, 'c':12}
print(mydict)

tmp = list()
for k, v in mydict.items():
    tmp.append( (v, k) )

print(tmp)

tmp = sorted(tmp, reverse = True)

print(tmp)
