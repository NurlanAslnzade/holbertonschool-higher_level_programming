#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        try:
            element = my_list[i]
            print("{:d}".format(element), end="")
            count += 1
        except IndexError:
            raise
        except (TypeError, ValueError):
            pass
        finally:
            i += 1
    print()
    return count
