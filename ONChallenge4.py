
#Allow user to enter a times table (only up to table 12)
# and a number of rows (5) to display.

number = int(input("Display the multiplication table for:"))

while number > 12:
    print("Invalid table number. Please use 1-12")
    number = int(input("Display the multiplication table for:"))
else:
    for i in range(0,5):
        print(number,"x",i,"=",number*i)


