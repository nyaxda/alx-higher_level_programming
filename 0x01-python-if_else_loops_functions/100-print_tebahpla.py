#!/usr/bin/python3
ch = ""
for i in range(122,96, -1):
    if i % 2 != 0:
        ch += chr(i - 32)
    else:
        ch += chr(i)
print("{}".format(ch), end = "")
