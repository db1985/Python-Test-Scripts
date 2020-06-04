#create a basic calculator

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))

choice = input("Enter +, -, *, /:")

if choice == "+":
    result = num1 + num2
elif choice == "-":
    result = num1 - num2
elif choice == "*":
    result = num1 * num2
elif choice == "/":
    result = num1 / num2
else:
    print("Wrong option!")
    
print(num1,choice,num2,"=",result)
