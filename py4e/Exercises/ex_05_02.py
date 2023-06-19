count = 0
total = 0
smallest = None
largest = None


while True:

    str_input = input ("Enter a number: ")

    if str_input == 'done':
        break

    try:
        number = int(str_input)
    except:
        print("Invalid Input")
        continue

    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number

    if largest is None:
        largest = number
    elif number > largest:
        largest = number

    count = count + 1
    total = total + number

print("The count is", count)
print("The total is", total)
print("The smallest is", smallest)
print("The largest is", largest)
print("The average is", total/count)
