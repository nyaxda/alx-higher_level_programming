#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        my_keys = list(a_dictionary.keys())
        return max(my_keys)
