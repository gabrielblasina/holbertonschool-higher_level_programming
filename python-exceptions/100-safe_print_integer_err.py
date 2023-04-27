#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        int_value = int(value)
    except Exception:
        print("Exception: Unknown format code 'd' for object of type 'str'",
              file=stderr)
        return False
    print("{:d}".format(int_value))
    return True
