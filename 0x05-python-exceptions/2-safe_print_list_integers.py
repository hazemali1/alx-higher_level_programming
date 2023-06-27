#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    q = 0
    for s in range(x):
        try:
            print("{:d}".format(my_list[s]), end="")
            q = q + 1
        except Exception:
            pass
    print('')
    return q
