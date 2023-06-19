def computepay(fhours, frate):
    if fhours <= 40:
        pay = fhours * frate
    else:
        overtime_hours = fhours - 40.0
        pay = (40.0 * frate) + (overtime_hours * frate * 1.5)
    return pay


str_hours = input ("Please enter hours: ")
str_rate = input ("Please enter rate: ")

try:
    hours = float(str_hours)
    rate = float(str_rate)
except:
    print("Error, please enter numeric input")
    quit()


print ("The pay is", computepay(hours, rate))
