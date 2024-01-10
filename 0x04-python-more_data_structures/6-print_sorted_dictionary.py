#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        b_key = sorted(a_dictionary.keys())
        for key in b_key:
            print(f"{key}: {a_dictionary[key]}")
