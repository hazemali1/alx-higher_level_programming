#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    s = []
    for d, w in zip(my_list_1, my_list_2):
        try:
            u = d / w
            if len(s) < list_length:
                s = s + [u]
        except TypeError:
            print('wrong type')
            if len(s) < list_length:
                s = s + [0]
        except ZeroDivisionError:
            print('division by 0')
            if len(s) < list_length:
                s = s + [0]
        finally:
            pass
    if len(my_list_1) != len(my_list_2):
        print('out of range')
        if len(s) < list_length:
            s = s + [0]
    return s
