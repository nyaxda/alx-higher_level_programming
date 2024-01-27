#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            final = (text[start:i + 1].strip())
            if final:
                print(final)
            start = i + 1
    print(text[start:].strip())
