#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    weight, score = 0, 0
    for t in my_list:
        weight += t[1]
        score += t[0] * t[1]
    return score / weight
