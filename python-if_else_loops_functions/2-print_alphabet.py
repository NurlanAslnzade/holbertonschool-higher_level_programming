#!/usr/bin/python3
a = ""
for i in range (97, 123):
    if chr(i) != "e" and chr(i) != "q":
        a += chr(i)
print("{}".format(a), end="")
