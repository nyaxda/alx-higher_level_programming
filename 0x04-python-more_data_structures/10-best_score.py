#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        maxim = next(iter(a_dictionary))
        for i in a_dictionary:
            if  i > maxim:
                maxim = i
        return maxim
