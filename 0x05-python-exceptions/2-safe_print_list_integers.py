#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    q = 0
    for s in range(x):
        try:
            print("{:d}".format(my_list[s]), end="")
            q = q + 1
        except ValueError:
            pass
    print('')
    return q
