#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    q = 0
    for s in range(x):
        try:
            if type(my_list[s]) == int:
                print("{:d}".format(my_list[s]), end="")
                q = q + 1
        except IndexError:
            pass
    print('')
    return q
