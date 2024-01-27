#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            print(text[start:i + 1].strip() + "\n")
            if i != len(text) - 1:
                print("\n")
            start = i + 1
    print(text[start:].strip())
