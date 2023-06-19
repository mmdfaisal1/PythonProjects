count = 0
total = 0
flag = True


while True:

    str_input = input ("Enter a number: ")

    if str_input == 'done':
        break

    try:
        number = int(str_input)
    except:
        print("Invalid Input")
        continue

    count = count + 1
    total = total + number

print("The count is", count)
print("The total is", total)
print("The average is", total/count)
