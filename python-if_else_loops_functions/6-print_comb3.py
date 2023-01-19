#!/usr/bin/python3
for number in range(1, 90):
    if (number < 10):
        print("{:02d}".format(number), end=", ")
    if (number > 10 and number < 89):
        if ((number / 10) < (number % 10)):
            print("{}".format(number), end=", ")
        else:
            continue
    if (number == 89):
        print("{}".format(number))
