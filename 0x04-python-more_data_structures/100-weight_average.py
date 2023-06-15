#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        d = 0
        s = 0
        for i in my_list:
            d += i[0] * i[1]
            s += i[1]
        return d / s
    else:
        return 0
