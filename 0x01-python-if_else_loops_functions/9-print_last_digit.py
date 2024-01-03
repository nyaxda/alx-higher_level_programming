#!/usr/bin/python3
def print_last_digit(number):
    numb = abs(number)
    last = numb % 10
    print("{}".format(last), end="")
    return last
