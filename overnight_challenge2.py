#Overnight challenge 2 Jun 20

#Pre-requisites

import math

#Allow user to enter length, width and height of their room.

print("Welcome to Dave's paint coverage calculator")

room_width = float(input("Please enter the width of your room in metres:"))

room_length = float(input("Please enter the length of your room in metres:"))
                    
room_height = float(input("Please enter the height of your room in metres:"))

#Calculate number of cans of paint needed based on 5m2 per can

paint_required = ((room_width * room_height) * 2) + ((room_length * room_height) *2)
                    
cans_required = math.ceil(paint_required / 5)

#Tell customer the number of tins of paint needed and the cost

print("The surface area you will need paint is",paint_required,"metres squared")
print("You will need",cans_required,"cans of paint for one coat")

#Ask customer how many coats of paint are they planning to use

number_coats = int(input("How many coats of paint will you use for the room?"))

paint_required_multiple_coats = paint_required * number_coats
                   
cans_required_multiple_coats = math.ceil(paint_required_multiple_coats / 5)
                   
print("You will need",cans_required_multiple_coats,"cans of paint")

                     


