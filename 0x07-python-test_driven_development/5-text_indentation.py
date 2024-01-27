#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    lines = text.split('\n')
    lines = [line.strip() for line in lines]
    text = '\n'.join(lines)
    print(text.strip(), end="")
