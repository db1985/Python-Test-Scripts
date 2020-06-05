#inch to cm

def inch_cm(number):
    conversion = number * 2.54
    return conversion

mynum = float(input("Enter a number in inches:"))
result = inch_cm(mynum)
print(f"{mynum} in inches is {result} in cm")
