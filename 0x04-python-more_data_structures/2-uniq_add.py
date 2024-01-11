#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    else:
        my_unique_list = set(my_list)
        count = 0
        for i in my_unique_list:
            count += i
        return count
