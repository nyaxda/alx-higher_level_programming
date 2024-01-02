#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = abs(number)
str = number % 10
if number >= 0:
    if str > 5:
        print(f"Last digit of {number} is {str} and is greater than 5")
    elif str == 0:
        print(f"Last digit of {number} is {str} and is 0")
    else:
        print(f"Last digit of {number} is {str} and is less than 6 and not 0")
else:
    str = -(temp % 10)
    print(f"Last digit of {number} is {str} and is less than 6 and not 0")
