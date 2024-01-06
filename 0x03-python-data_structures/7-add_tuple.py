#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        a = int(tuple_a[0])
        b = 0
    elif not tuple_a or tuple_a is None:
        a = 0
        b = 0
    else:
        a = int(tuple_a[0])
        b = int(tuple_a[1])
    if len(tuple_b) == 1:
        c = int(tuple_b[0])
        d = 0
    elif not tuple_b or tuple_b is None:
        c = 0
        d = 0
    else:
        c = int(tuple_b[0])
        d = int(tuple_b[1])
    tuple_c = (a+c, b+d)
    return (tuple_c)
