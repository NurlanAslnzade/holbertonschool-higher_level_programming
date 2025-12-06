#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for i in range(x):
        try:
            print(("{}".format(i))
            a += 1
        except (Type Error):
            pass
        print()
        return a
