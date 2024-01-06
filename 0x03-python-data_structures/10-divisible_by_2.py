#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or not my_list:
        return None
    else:
        cond = []
        for i in my_list:
            if i % 2 == 0:
                cond.append(True)
            else:
                cond.append(False)
        return cond

