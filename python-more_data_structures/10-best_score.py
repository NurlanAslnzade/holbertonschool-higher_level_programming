#!/usr/bin/python3
def best_score(a_dictionary):
    a = []
    for key, value in a_dictionary.items():
        a.append(value)
    if len(a) > 0:
        return max(a)
    else:
        return None
