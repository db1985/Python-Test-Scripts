#inch to cm

def inch_to_cm(number):
    conversion = number * 2.54
    return conversion

mynum = float(input("Enter a number in inches:"))
result = inch_to_cm(mynum)
print(f"{mynum} in inches is {result} in cm")

#cm to inch

def cm_to_inch(number):
    conversion = number / 2.54
    return conversion

mynum = float(input("Enter a number in cm:"))
result = cm_to_inch(mynum)
print(f"{mynum} in cm is {result} in inches")
