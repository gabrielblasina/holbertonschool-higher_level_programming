#!/usr/bin/python3
import random
last_number = 0
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is", end=" ")
if (number >= 0):
    last_number = number % 10
if (number < 0):
    last_number = (number * -1) % 10
if (last_number > 5):
    if (number > 0):
        print(f"{last_number} and is greater than 5")
    if (number < 0):
        print(f"-{last_number} and is less than 6 and not 0")
elif (last_number < 6 and last_number != 0):
    if (number > 0):
        print(f"{last_number} and is less than 6 and not 0")
    if (number < 0):
        print(f"-{last_number} and is less than 6 and not 0")
else:
    print(f"{last_number} and is 0")
