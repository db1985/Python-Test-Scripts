#Overnight challenge 3

#Pre-requisites

import re

#Allow user to enter a sequence of text. Eliminate difference between upper and lower.

usertext = input("Please describe the street where you live, using at least three words:")

lower_usertext = usertext.lower()

count = 0

#Should count how many times each vowel occurs.

for v in lower_usertext:
    if (v=="a" or v=="e" or v=="i" or v=="o" or v=="u"):
        print(lower_usertext.count(v))





