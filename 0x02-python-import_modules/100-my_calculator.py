#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
def calc_argv(argv):
    args = len(argv) - 1
    if args != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
    operator_list = "+-*/"
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator in operator_list:
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        else:
            result = div(a, b)
            #print("{:d} {:s} {:d} = {:f}".format(a, operator, b, div(a, b)))
        print("{} {} {} = {}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")

if __name__ == "__main__":
    from sys import argv
    calc_argv(argv)
