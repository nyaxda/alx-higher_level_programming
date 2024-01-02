#!/usr/bin/python3
def uppercase(str):
    ch = ""
    for w in str:
        if ord(w) >= 97 and ord(w) <= 122:
            w = chr(ord(w) - 32)
        ch += w
    print("{}".format(ch))
