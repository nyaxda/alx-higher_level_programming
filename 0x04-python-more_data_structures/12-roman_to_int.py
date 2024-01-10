#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    romanint = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    final = 0
    prev = 0

    for roman in reversed(roman_string):
        value = romanint[roman]

        if value >= prev:
            final += value
        else:
            final -= value

        prev = value

    return final
