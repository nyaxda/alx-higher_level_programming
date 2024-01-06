#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "" or sentence is None:
        a = None
    else:
        a = sentence[0]
    b = len(sentence)
    c = (b, a)
    return c
