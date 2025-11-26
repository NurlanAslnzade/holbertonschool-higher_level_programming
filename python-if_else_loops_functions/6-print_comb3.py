#!/usr/bin/python3
for i in range(0, 10):
    for h in range(i+1, 10):
        if i*10 + h !=89:
            print("{0:02d}".format(i*10 + h), end=(", "))
print(89)
