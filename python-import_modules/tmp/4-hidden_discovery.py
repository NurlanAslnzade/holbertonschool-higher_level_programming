#!/usr/bin/python3

import sys
import hidden_4

for i in dir(hidden_4):
    if i[0] != "_":
        print(i)
