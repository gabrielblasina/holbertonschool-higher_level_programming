#!/usr/bin/python3
def uppercase(str):
    is_upper = ''  # This will give the format of str
    for character in str:
        if ord(character) > 96 and ord(character) < 123:
            is_upper += chr(ord(character) - 32)  # we need to typecast it
        else:
            is_upper += character
    print("{}".format(is_upper))
