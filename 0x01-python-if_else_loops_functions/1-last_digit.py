#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if last == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif last < 6 and last != 0:
    if number < 0:
        print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last} and greater than 5")
