#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    a = 0
    b = 0

    rum_number = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    for i in reversed(roman_string):
        value = rum_number.get(i, 0)
        if value < b:
            a -= value
        else:
            a += value
        b = value

    return a
