#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    values = my_list.value()
    map(lambda x: x * 2, values)
    return my_list
