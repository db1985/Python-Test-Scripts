#test a user's password

SECRET = "letmein"
password = None

#loop which works whilst password is not right:

while password != SECRET:
    password = input("Enter your password:")

#check the password entered by the user

    if password != SECRET:
        print("Password incorrect!")

print("Welcome!")
