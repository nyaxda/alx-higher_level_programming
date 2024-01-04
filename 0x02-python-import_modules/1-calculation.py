#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    ad = add(a, b)
    su = sub(a, b)
    mu = mul(a, b)
    di = div(a, b)
    print("{} + {} = {}".format(a, b, ad))
    print("{} - {} = {}".format(a, b, su))
    print("{} * {} = {}".format(a, b, mu))
    print("{} / {} = {}".format(a, b, di))


if __name__ == "__main__":
    main()
