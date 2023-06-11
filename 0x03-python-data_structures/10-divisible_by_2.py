#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for m in my_list:
        if m % 2 == 0:
            res += "True"
        else:
            res += "False"
    return (res)
