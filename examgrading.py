#Allow user to enter exam mark

student_mark = input(int("Please enter your exam mark:"

#Marking

if student_mark > 0 and student_mark < 40:
    print("Epic Fail")

elif student_mark > 39 and student_mark < 65:
    print("Pass. Good Effort")

elif student_mark > 64 and student_mark < 80:
    print("Merit. Good job")

else student_mark > 80:
    print("Distinction. Awesome!")
    
                         
