# 3 people number between 1 - 100
# 3 number input program tell which is closest

import random

varun_number = int(input("Number Varun?\n\r"))
robby_number = int(input("Number? Robby?\n\r"))
chris_number = int(input("Number chris?\n\r"))

actual_number = random.randrange(1, 101)

varun_distance = varun_number - actual_number
robby_distance = robby_number - actual_number
chris_distance = chris_number - actual_number

if varun_distance < 0:
    varun_distance = varun_distance * -1
if robby_distance < 0:
    robby_distance = robby_distance * -1
if chris_distance < 0:
    chris_distance = chris_distance * -1

if varun_distance < robby_distance:
    lower_distance_1 = varun_distance
else:
    lower_distance_1 = robby_distance
if lower_distance_1 < chris_distance:
    lowest_distance = lower_distance_1
else:
    lowest_distance = chris_distance

if lowest_distance == chris_distance:
    winner = "Chris"
elif lowest_distance == robby_distance:
    winner = "Robby"
elif lowest_distance == varun_distance:
    winner = "Varun"
print("The actual number {number}".format(number=actual_number))
print(winner)