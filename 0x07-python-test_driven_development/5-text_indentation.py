#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        c = 0
        while c < len(text) and text[c] == ' ':
            c += 1
        while c < len(text):
            print(text[c], end="")
            if text[c] == "\n" or text in ".?:":
                if text[c] in ".?:":
                    print("\n")
                c += 1
                while c < len(text) and text[c] == ' ':
                    c += 1
                continue
            c += 1
