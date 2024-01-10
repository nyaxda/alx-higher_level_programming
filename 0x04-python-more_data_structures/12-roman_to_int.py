#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0
    else:
        roman_to_num = {
                'I': 1,
                'II': 2,
                'III': 3,
                'IV': 4,
                'V': 5,
                'VI': 6,
                'VII': 7,
                'VIII': 8,
                'IX': 9,
                'X': 10,
                'XX': 20,
                'XXX': 30,
                'XL': 40,
                'L': 50,
                'LX': 60,
                'LXX': 70,
                'LXXX': 80,
                'XC': 90,
                'C': 100,
                'CC': 200,
                'CCC': 300,
                'CD': 400,
                'D': 500,
                'DC': 600,
                'DCC': 700,
                'DCCC': 800,
                'CM': 900,
                'M': 1000,
                'MM': 2000,
                'MMM': 3000
        }
        split_symbols = []
        i = 0
        while i < len(roman_string):
            found = False
            for key in sorted(roman_to_num.keys(), reverse=True):
                if roman_string[i:i+len(key)] == key:
                    split_symbols.append(key)
                    i += len(key)
                    found = True
                    break
            if not found:
                return 0
        sum = 0
        if split_symbols:
            for i in split_symbols:
                sum += roman_to_num[i]
        return sum
