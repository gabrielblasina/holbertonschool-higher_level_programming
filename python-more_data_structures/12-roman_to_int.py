#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    if type(roman_string) != str or roman_string is None:
        return 0
    for letter in reversed(roman_string):
        curr_value = rom_dic[letter]
        if curr_value >= prev_value:
            result += curr_value
        else:
            result -= curr_value
        prev_value = curr_value
    return result
