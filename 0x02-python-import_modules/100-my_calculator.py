#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            res = add(a, b)
        elif sys.argv[2] == "-":
            res = sub(a, b)
        elif sys.argv[2] == "*":
            res = mul(a, b)
        elif sys.argv[2] == "/":
            res = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}".format(a, sys.argv[2], b, res))
        sys.exit(0)


if __name__ == "__main__":
    main()
