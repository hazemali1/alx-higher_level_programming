#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for n in my_string:
        if n != 'c' and n != 'C':
            string += n
    return (string)
