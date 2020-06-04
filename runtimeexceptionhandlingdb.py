#get an input with runtime exception handling

try:
    age = int(input("Enter age:"))
except ValueError:
    print("That's not a valid age")
else:
    print(f"You are", age, "years old")
