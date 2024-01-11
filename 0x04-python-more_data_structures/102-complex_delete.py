#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or not a_dictionary:
        return None
    else:
        b_dictionary = {}
        keys_to_delete = []
        for key, delete in a_dictionary.items():
            if delete == value:
                keys_to_delete.append(key)
        for key in keys_to_delete:
            del a_dictionary[key]
    return a_dictionary
