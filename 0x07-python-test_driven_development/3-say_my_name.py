#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>"""
    if type(first name) is not str or first name is None:
        raise TypeError("first_name must be a string")
    if type(last name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
