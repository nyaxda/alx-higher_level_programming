#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>"""
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    tfirst = first_name.strip()
    if tfirst == "":
        raise TypeError("first_name must be a string")
    if last_name and last_name != "":
        tlast = last_name.strip()
        print("My name is {} {}".format(tfirst, tlast))
    else:
        print("My name is {}".format(tfirst))
