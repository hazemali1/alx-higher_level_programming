#!/usr/bin/python3
def no_c(my_string):
    for n in range(len(my_string) - 1):
        if my_string[n] == 'c' or my_string[n] == 'C':
            my_string[n] = []
    return (my_string)
