#!/usr/bin/python3
def roman_to_int(roman_string):
    s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    d = 0
    if roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if len(roman_string) == 1:
            return s[roman_string[i]]
        elif i == len(roman_string) - 1:
            d += s[roman_string[i]]
        elif s[roman_string[i]] >= s[roman_string[i + 1]]:
            d += s[roman_string[i]]
        elif s[roman_string[i]] < s[roman_string[i + 1]]:
            d -= s[roman_string[i]]
    return d
