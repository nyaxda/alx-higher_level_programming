#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0
    else:
        roman_to_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        final = 0
        for i in reversed(roman_string):
            number = roman_to_num[i]
            if number >= prev:
                final += number
            else:
                final -= number
            prev = number
        return final
