#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or not my_list:
        return 0
    else:
        total = 0
        wtotal = 0
        for i in my_list:
            a, b = i
            total += b
            wtotal += a * b
        return wtotal / total
