#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    s = number % -10
else:
    s = number % 10
if s > 5:
    d = "and is greater than 5"
elif s == 0:
    d = "and is 0"
elif s < 6 and s != 0:
    d = "and is less than 6 and not 0"
print("Last digit of", number, "is", s, d)
