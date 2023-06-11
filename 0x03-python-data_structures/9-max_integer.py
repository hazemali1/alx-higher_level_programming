#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        d = my_list[0]
        for s in my_list:
            if s > d:
                d = s
        return d
    else:
        return ("None")
