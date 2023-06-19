# with open("scan_names.txt", "r") as fh:
#     lines = fh.read().splitlines()

with open("path_names.txt", "r") as fh:
    path_names_list = fh.read().splitlines()

i = 1
print(path_names_list[(i*3)],path_names_list[(i*3)+1],path_names_list[(i*3)+2])

#print(lines)
