#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for n in range(x):
        try:
            print('{:d}'.format(my_list[n]), end='')
            total += 1
        except (TypeError, ValueError):
            continue
    print()
    return total
