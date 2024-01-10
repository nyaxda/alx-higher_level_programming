#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        maxim = None
        for i in a_dictionary:
            if maxim is None or i > maxim:
                maxim = i
        return maxim
