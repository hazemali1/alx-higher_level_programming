#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    s = []
    for d, w in zip(my_list_1, my_list_2):
        try:
            s = s + [d / w]
        except TypeError:
            print('wrong type')
            s = s + [0]
        except ZeroDivisionError:
            print('division by 0')
            s = s + [0]
        finally:
            pass
    if len(my_list_1) != len(my_list_2):
        print('out of range')
        s = s + [0]
    return s
