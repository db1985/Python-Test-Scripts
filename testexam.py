#Allow user to enter exam mark

student_mark = int(input("Please enter your exam mark:"))

#Marking

if student_mark < 40:
    print("Epic Fail")

elif student_mark < 65:
    print("Pass. Good Effort")

elif student_mark < 80:
    print("Merit. Good job")

else student_mark < 101:
    print("Distinction. Awesome!")
    
                         
