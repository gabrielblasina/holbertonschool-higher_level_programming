#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_new_list = []
    for index in range(0, (len(my_list) - 1)):
        if (my_list[index] % 2 == 0):
            my_new_list.append(True)
        else:
            my_new_list.append(False)
    return (my_new_list)
