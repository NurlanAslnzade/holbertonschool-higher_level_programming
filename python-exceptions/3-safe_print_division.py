#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        if b != 0:
            result = a/b
    except:
        result = None
    finally:
        print("{:d} / {:d} = {}".format(a, b, result))
    return result
