hours = input ("Please enter hours: ")
rate = input ("Please enter rate: ")

if float(hours) <= 40:
    pay = float(hours) * float(rate)
else:
    overtime_hours = float(hours) - 40.0
    pay = (40.0 * float(rate)) + (overtime_hours * float(rate) * 1.5)

print ("The pay is", pay)
