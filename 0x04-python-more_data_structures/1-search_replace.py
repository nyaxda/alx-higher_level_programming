#!/usr/bin/python3
def replacer(search, replace, x):
    return replace if x == search else x


def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    elif search is None or replace is None:
        return my_list
    else:
        return list(map(lambda x: replacer(search, replace, x), my_list))
