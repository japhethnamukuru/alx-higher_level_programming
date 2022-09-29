#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i,c in enumerate(roman_string):
        if (i+1) == len(roman_string) or roman_numerals[c] >= roman_numerals[roman_string[i+1]]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    return result
