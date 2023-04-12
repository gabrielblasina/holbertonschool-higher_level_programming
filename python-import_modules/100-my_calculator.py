#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import sub, add, mul, div

    operations = {'-': sub, '+': add, '*': mul, '/': div}

    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    ops = argv[2]

    if ops not in list(operations.keys()):
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    result = operations[ops](a, b)
    print(f'{a} {ops} {b} = {result}')