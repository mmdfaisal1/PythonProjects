str_hours = input ("Please enter hours: ")
str_rate = input ("Please enter rate: ")

try:
    hours = float(str_hours)
    rate = float(str_rate)
except:
    print("Error, please enter numeric input")
    quit()


if hours <= 40:
    pay = hours * rate
else:
    overtime_hours = hours - 40.0
    pay = (40.0 * rate) + (overtime_hours * rate * 1.5)

print ("The pay is", pay)
